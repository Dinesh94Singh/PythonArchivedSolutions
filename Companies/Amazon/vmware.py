#!/bin/python3

import sys
import os
import requests
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json


# Complete the function below.
# Base url: https://jsonmock.hackerrank.com/api/movies/search/?Title=

def getMovieTitles(substr):
    BASE_URL = "https://jsonmock.hackerrank.com/api/movies/search/?Title={}".format(substr)

    # TODO Made a service call to retrive the JSON

    data = requests.get(url=BASE_URL).json()
    total_number_of_pages = data['total_pages']

    res = []
    for i in range(total_number_of_pages):
        PAGE_URL = "https://jsonmock.hackerrank.com/api/movies/search/?Title={}&page={}".format(substr, i + 1)
        results = requests.get(url=PAGE_URL).json()
        for each in results['data']:
            res.append(each['Title'])

    res = sorted(res)
    return res


f = open(os.environ['OUTPUT_PATH'], 'w')

try:
    _substr = str(input())
except:
    _substr = None

res = getMovieTitles(_substr)
for res_cur in res:
    f.write(str(res_cur) + "\n")

f.close()
