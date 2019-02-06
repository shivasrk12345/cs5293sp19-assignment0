from typing import List, Dict, Any
import random
from urllib.request import urlopen as ureq
import json
url = "https://raw.githubusercontent.com/TrumpTracker/trumptracker.github.io/master/_data/data.json"
def download():
    uclient=ureq(url).read()
    return uclient
def extract_requests(text):
    result=json.loads(text)
    listofpromises= result['promises']
    return listofpromises
def extract_titles(lop):
    listoftitles = []
    for i in range(len(lop)):
        listoftitles.append(lop[i]['title'])
    return listoftitles
def random_title(lot):
    randomtitle=random.choice(lot)
    return randomtitle



