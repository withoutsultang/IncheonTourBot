import os
import openai
import pandas as pd
import faiss
import numpy as np

csv_file = './chatbot/tourInfo.csv'

API_KEY = "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"
openai.api_key = API_KEY

chat_model = "gpt-3.5-turbo"
system_message = "너는 인천 여행 가이드야. 인천 여행 가이드라고 소개하고 모르는 답변이 있으면 고객센터 1234-5678로 연락달라 그래."

# os.environ["OPENAI_API_KEY"] = "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"
# openai.api_key = os.environ["OPENAI_API_KEY"]
# def load_csv():
#     df = pd.read_csv(csv_file, dtype=str)
#
#     df['addr1'] = df['addr1'].astype(str)
#
#     return df

def create_faiss_index():
    df = pd.read_csv("./chatbot/tourInfo.csv", dtype=str)

    embeddings = df['addr1'].astype(str).apply(get_embedding).tolist()

    embeddings = np.vstack(embeddings)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return df, index

def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    embedding = openai.Embedding.create(input=[text], model=model)
    return embedding['data'][0]['embedding']

def search_similar_documents(embedding, index, k=1):
    D, I = index.search(np.array([embedding]), k)
    return I[0][0]

def generate_response(user_input, df, index, system_message, chat_history=None):

    user_embedding = get_embedding(user_input)

    _, I = index.search(np.array([user_embedding]), 1)
    similar_document = df.iloc[I[0][0]]['addr1']

    system_message += " " + similar_document
    #
    messages = [
        {"role": "system", "content": system_message}, #+ chat_history},
        {"role": "user", "content": user_input}
    ]

    response = openai.ChatCompletion.create(
        model=chat_model,
        messages=messages
    )

    return response['choices'][0]['message']['content']

def chatbot_backend(user_input, system_message, chat_history=None):
    df, index = create_faiss_index()
    response = generate_response(user_input, df, index, system_message, chat_history)
    return response

def main():
    # df = load_csv()
    #
    # embeddings = [get_embedding(text) for text in df['addr1']]
    #
    # d = embeddings[0].shape[0]
    # index = faiss.IndexFlatL2(d)
    # index.add(np.array(embeddings))
    #
    # chat_history = ""

    while True:
        user_input = input("입력 : ")

        response = chatbot_backend(user_input,
                                   system_message="You are a friendly Incheon travel guide. Introduce yourself as an Incheon travel guide, and if you don't know the answer, please contact customer center 1234-5678.") #chat_history)

        print("출력 : ", response)

        # chat_history += '\n' + user_input + '\n' + response


if __name__ == "__main__":
    main()
