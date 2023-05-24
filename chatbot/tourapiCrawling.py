import os

import pandas
from bs4 import BeautifulSoup
import requests
import json
import time

# tourapiCrawling.py
# tourapi에서 관광지 정보를 크롤링하는 함수

def tourapiCrawling():

    data = list()


    # for i in range(1, 168):
    #     data.append(str(i))

    key = "RoA41VMcoHYDwXimSIrf%2Fz1qZ3Bf76THkiDp0MVD8NZchLHLkwnMeMXbL6ZCdVZ9JlIjHmaC%2BCQ4c%2FWJJpU5%2FA%3D%3D"

    for i in range(1, 168):
        endpoint = "http://apis.data.go.kr/B551011/KorService1/areaBasedList1?numOfRows=12&pageNo={}&MobileOS=ETC&MobileApp=AppTest&ServiceKey={}&listYN=Y&arrange=A&contentTypeId=&areaCode=2&sigunguCode=&cat1=&cat2=&cat3=".format(
            str(i), key)

        req = requests.get(endpoint)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        item_list = soup.findAll('item')

        addr1_list = []
        addr2_list = []
        areacode_list = []
        booktour_list = []
        cat1_list = []
        cat2_list = []
        cat3_list = []
        contentid_list = []
        contenttypeid_list = []
        createdtime_list = []
        firstimage_list = []
        firstimage2_list = []
        # cpyrhtDivCd_list = []
        mapx_list = []
        mapy_list = []
        mlevel_list = []
        modifiedtime_list = []
        sigungucode_list = []
        tel_list = []
        title_list = []
        zipcode_list = []

        for item in item_list:
            addr1 = item.find('addr1').text
            addr1_list.append(addr1)
            addr2 = item.find('addr2').text
            addr2_list.append(addr2)
            areacode = item.find('areacode').text
            areacode_list.append(areacode)
            booktour = item.find('booktour').text
            booktour_list.append(booktour)
            cat1 = item.find('cat1').text
            cat1_list.append(cat1)
            cat2 = item.find('cat2').text
            cat2_list.append(cat2)
            cat3 = item.find('cat3').text
            cat3_list.append(cat3)
            contentid = item.find('contentid').text
            contentid_list.append(contentid)
            contenttypeid = item.find('contenttypeid').text
            contenttypeid_list.append(contenttypeid)
            createdtime = item.find('createdtime').text
            createdtime_list.append(createdtime)
            firstimage = item.find('firstimage').text
            firstimage_list.append(firstimage)
            firstimage2 = item.find('firstimage2').text
            firstimage2_list.append(firstimage2)
            # cpyrhtDivCd = item.find('cpyrhtDivCd').text
            # cpyrhtDivCd_list.append(cpyrhtDivCd)
            mapx = item.find('mapx').text
            mapx_list.append(mapx)
            mapy = item.find('mapy').text
            mapy_list.append(mapy)
            mlevel = item.find('mlevel').text
            mlevel_list.append(mlevel)
            modifiedtime = item.find('modifiedtime').text
            modifiedtime_list.append(modifiedtime)
            sigungucode = item.find('sigungucode').text
            sigungucode_list.append(sigungucode)
            tel = item.find('tel').text
            tel_list.append(tel)
            title = item.find('title').text
            title_list.append(title)
            zipcode = item.find('zipcode').text
            zipcode_list.append(zipcode)

        for addr1, addr2, areacode, booktour, cat1, cat2, cat3, contentid, contenttypeid, createdtime, firstimage, firstimage2, mapx, mapy, mlevel, modifiedtime, sigungucode, tel, title, zipcode \
                in zip(addr1_list, addr2_list, areacode_list, booktour_list, cat1_list, cat2_list, cat3_list, contentid_list, contenttypeid_list, createdtime_list, firstimage_list, firstimage2_list, mapx_list, mapy_list, mlevel_list, modifiedtime_list, sigungucode_list, tel_list, title_list, zipcode_list):
            row_data = [addr1, addr2, areacode, booktour, cat1, cat2, cat3, contentid, contenttypeid, createdtime, firstimage, firstimage2, mapx, mapy, mlevel, modifiedtime, sigungucode, tel, title, zipcode]
            data.append(row_data)
        # try:
        #     addr1 = soup.select('addr1')[0].text
        #     addr1_list.append(addr1)
        #     addr2 = soup.select('addr2')[0].text
        #     addr2_list.append(addr2)
        #     areacode = soup.select('areacode')[0].text
        #     areacode_list.append(areacode)
        #     booktour = soup.select('booktour')[0].text
        #     booktour_list.append(booktour)
        #     cat1 = soup.select('cat1')[0].text
        #     cat1_list.append(cat1)
        #     cat2 = soup.select('cat2')[0].text
        #     cat2_list.append(cat2)
        #     cat3 = soup.select('cat3')[0].text
        #     cat3_list.append(cat3)
        #     contentid = soup.select('contentid')[0].text
        #     contentid_list.append(contentid)
        #     contenttypeid = soup.select('contenttypeid')[0].text
        #     contenttypeid_list.append(contenttypeid)
        #     createdtime = soup.select('createdtime')[0].text
        #     createdtime_list.append(createdtime)
        #     firstimage = soup.select('firstimage')[0].text
        #     firstimage_list.append(firstimage)
        #     firstimage2 = soup.select('firstimage2')[0].text
        #     firstimage2_list.append(firstimage2)
        #     cpyrhtDivCd = soup.select('cpyrhtDivCd')[0].text
        #     cpyrhtDivCd_list.append(cpyrhtDivCd)
        #     mapx = soup.select('mapx')[0].text
        #     mapx_list.append(mapx)
        #     mapy = soup.select('mapy')[0].text
        #     mapy_list.append(mapy)
        #     mlevel = soup.select('mlevel')[0].text
        #     mlevel_list.append(mlevel)
        #     modifiedtime = soup.select('modifiedtime')[0].text
        #     modifiedtime_list.append(modifiedtime)
        #     sigungucode = soup.select('sigungucode')[0].text
        #     sigungucode_list.append(sigungucode)
        #     tel = soup.select('tel')[0].text
        #     tel_list.append(tel)
        #     title = soup.select('title')[0].text
        #     title_list.append(title)
        #     zipcode = soup.select('zipcode')[0].text
        #     zipcode_list.append(zipcode)
        #
        # except Exception as e:
        #     print(e)

        # tourInfo = {}
        # tourInfo['addr1'] = addr1_list
        # tourInfo['addr2'] = addr2_list
        # tourInfo['areacode'] = areacode_list
        # tourInfo['booktour'] = booktour_list
        # tourInfo['cat1'] = cat1_list
        # tourInfo['cat2'] = cat2_list
        # tourInfo['cat3'] = cat3_list
        # tourInfo['contentid'] = contentid_list
        # tourInfo['contenttypeid'] = contenttypeid_list
        # tourInfo['createdtime'] = createdtime_list
        # tourInfo['firstimage'] = firstimage_list
        # tourInfo['firstimage2'] = firstimage2_list
        # tourInfo['cpyrhtDivCd'] = cpyrhtDivCd_list
        # tourInfo['mapx'] = mapx_list
        # tourInfo['mapy'] = mapy_list
        # tourInfo['mlevel'] = mlevel_list
        # tourInfo['modifiedtime'] = modifiedtime_list
        # tourInfo['sigungucode'] = sigungucode_list
        # tourInfo['tel'] = tel_list
        # tourInfo['title'] = title_list
        # tourInfo['zipcode'] = zipcode_list

        df = pandas.DataFrame(data, columns=['addr1', 'addr2', 'areacode', 'booktour', 'cat1', 'cat2', 'cat3', 'contentid', 'contenttypeid', 'createdtime', 'firstimage', 'firstimage2', 'mapx', 'mapy', 'mlevel', 'modifiedtime', 'sigungucode', 'tel', 'title', 'zipcode'])
        # os.chdir("C:/Users")
        df.to_csv('tourInfo.csv', encoding='utf-8-sig')


tourapiCrawling()

