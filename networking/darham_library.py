import json
import requests


def process(link):
    proxies = {
        "http": None,
        "https": None,
    }
    response = requests.get(link)
    if response.status_code == 200:
        if len(response.json()) == 0:
            return "I can't recognize it"
        else:
            category = response.json()[0]['category']
            all_is_same = True
            for book in response.json():
                if book['category'] != category:
                    all_is_same = False
            if all_is_same:
                return category
            return "I can't recognize it"
    else:
        return "Bad Query"
