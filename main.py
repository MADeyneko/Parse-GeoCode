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

class Us:
    def __init__(self, path):
        self.path=path
        self.pd=pd.read_csv(path, sep=';')
        print(self.pd.head())

    def getUniqueAddress(self):
        self.pd['city_street']=self.pd['CITY']+' '+ self.pd['street']+' '+self.pd['found_house_number']
        return pd.unique(self.pd['city_street'])

if __name__=='__main__':
    us=Us('us.csv')
    unique_add=us.getUniqueAddress()
    print(unique_add)
    # g=geo.GeoCode(conf.API)
    # g.getGeo('колобок центральная')