import json
import requests

link = 'http://127.0.0.1:8000/'


def process(book):
    book_link = link + str(book['category']) + '/'
    response = requests.get(book_link)
    if book in response.json():
        return 'bad query'
    response = requests.post(book_link, book)
    return str(response)
