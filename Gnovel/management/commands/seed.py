import requests
import datetime
import hashlib
from django.core.management.base import BaseCommand
from ....gnovelapi.models import Comic

timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
pub_key = '3f68a813b04d0f4f73487c58ced1cc60'
pvt_key = 'c3fbfa2e298ac40a1d2d0ab3f3df265e8dc26e40'

def hash_params():
    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{pvt_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params

params = {'ts': timestamp, 'apikey': pub_key, 'hash': hash_params()};
res = requests.get('http://gateway.marvel.com/v1/public/comics', params=params)

results = res.json()


# def get_comics():
#     url = 'http://gateway.marvel.com/v1/public/comics?'
#     r = requests.get(url, headers={'Content-Type':
#         'application/json'})
#     comics = r.json()
#     return comics

def seed_comic():
