class GeoCode:
    def __init__(self, api):
        self.API=api

    def getGeoCode(self, address):   #Получаем геопозиции города
        url = 'https://geocode-maps.yandex.ru/1.x?geocode="'+address+'"&apikey='+self.API+'&format=json'
        resp = requests.get(url)
        resp = resp.json()['response']['GeoObjectCollection']['featureMember']
        if len(resp) > 0:
            return resp[0]['GeoObject']['boundedBy']['Envelope']
        else:
            print('NOT FOUND! --> ' + address)
            return '- -'
