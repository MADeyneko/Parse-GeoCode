import GeoCode as geo
import config as conf
import pandas as pd
import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import progressbar
import math 
import os
import sys
from bs4 import BeautifulSoup
from lxml import html
import urllib

class PBar:
    def __init__(self, desc:str, size: int):
        self.widgets=[
            desc
            , progressbar.Bar(left='', marker='▓', right='')
            , progressbar.SimpleProgress()
            , ' [',progressbar.Timer(), '] '
        ]
        self.bar=progressbar.ProgressBar(
            maxval=size,
            widgets=self.widgets).start()

class GeoAddress:

    def __init__(self):
        file=open('address_geocode', 'r+')
        self.add=self.get_address(file.read().splitlines())
        self.file=file
        self.list=[]
        self.geo=geo.GeoCode(conf.API)

    def get_address(self, rows):
        c=[]
        for value in rows:
            c.append(value.split(';')[0])

        return c

    def add_adress(self, list):
        self.bar=PBar('Added address:', len(list)).bar
        count=0
        try:
            for value in list[1:-1]:
                if (value in self.add)==False:
                    g=self.geo.getGeo(value)
                    self.add.append(value)
                    self.list.append(value+';'+g['lowerCorner']+';'+g['upperCorner'])
                count+=1
                self.bar.update(count)
        except :
            self.file_save()
            self.file.close()

    def file_save(self):
        for row in self.list:
            self.file.write("%s\n" % row)
        print("Save file \n")

    def __del__(self):
        self.file.close()

class Us:
    def __init__(self, path):
        self.path=path
        self.pd=pd.read_csv(path, sep=';')
        print(self.pd.head())

    def getUniqueAddress(self):
        self.pd['city_street']=self.pd['CITY']+', '+ self.pd['street']+', '+self.pd['found_house_number']
        return pd.unique(self.pd['city_street'])

if __name__=='__main__':
    us=Us('us.csv')
    unique_add=us.getUniqueAddress()
    ga=GeoAddress()
    ga.add_adress(unique_add)