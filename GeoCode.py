import requests

class GeoCode:
    def __init__(self, api):
        self.API=api

    def getGeo(self, address):   #Получаем геопозиции города
        url = 'https://geocode-maps.yandex.ru/1.x?geocode="'+address+'"&apikey='+self.API+'&format=json'
        resp = requests.get(url)
        resp = resp.json()['response']['GeoObjectCollection']['featureMember']
        if len(resp) > 0:
            return resp[0]['GeoObject']['boundedBy']['Envelope']
        else:
            print('NOT FOUND! --> ' + address)
            res=dict()
            res['lowerCorner']='-'
            res['upperCorner']='-'
            return res

    def getInfo(item):   #Получаем инфо об организации
        url = 'https://search-maps.yandex.ru/v1/?apikey='+self.API+'&text="'+item+'"&lang=ru_RU&type=biz'
        resp = requests.get(url)
        return resp.json()
