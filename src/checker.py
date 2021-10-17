# coding: UTF-8
# !/usr/bin/python

import os
import requests
from bs4 import BeautifulSoup
from notifier import notify

amazon_headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NP06; rv:11.0) like Gecko"
}
amazon_url = os.environ["AMAZON_URL"].split(',')

def check():
    for i in range(len(amazon_url)):
        url = amazon_url[i]
        data = requests.get(url, headers = amazon_headers)
        data.encoding = data.apparent_encoding
        data = data.text
        soup = BeautifulSoup(data, "html.parser")
        source = soup.select('#tabular-buybox > div.tabular-buybox-container > div:nth-child(4) > div > span > a')
        if source is None or len(source) < 1:
            return
        if source[0].string == 'Amazon.co.jp':
            price = soup.select('#price_inside_buybox')[0].string
            notify("販売元 Amazon.co.jp の在庫があります:{} {}".format(price, url))
