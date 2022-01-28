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

if __name__=='__main__':
    g=geo.GeoCode(conf.API)
    g.getGeo('колобок центральная')