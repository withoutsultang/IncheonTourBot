import openai

class GPTAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_response(self, prompt, model="text-davinci-003", max_tokens=50, n=1, stop=None, temperature=1.0):
        responine=model,se = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens,
            n=n,
            stop=stop,
            temperature=temperature
        )
        return response.choices[0].text.strip() if n == 1 else [choice.text.strip() for choice in response.choices]

if __name__ == "__main__":
    API_KEY = "your_openai_api_key"
    gpt = GPTAPI(api_key=API_KEY)

    prompt = "Translate the following English text to Korean: 'Hello, how are you?'"
    response = gpt.generate_response(prompt)

    print(f"Generated response: {response}")