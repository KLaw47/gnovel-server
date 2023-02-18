import requests
import datetime
import hashlib
from django.core.management.base import BaseCommand
from gnovelapi.models import Comic

timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
pub_key = '3f68a813b04d0f4f73487c58ced1cc60'
pvt_key = 'c3fbfa2e298ac40a1d2d0ab3f3df265e8dc26e40'

def hash_params():
    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{pvt_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params

params = {'ts': timestamp, 'apikey': pub_key, 'hash': hash_params()}
res = requests.get('http://gateway.marvel.com/v1/public/comics', params=params, headers={'Content-Type':
    'application/json'})

results = res.json()


def seed_comic():
    print(results)
    for c in results["data"]['results']:
        thumb_path = c["thumbnail"]["path"]
        comic = Comic(
            title=c["title"],
            description=c["description"],
            thumbnail=thumb_path + "/portrait_xlarge.jpg",
        )
        comic.save()

class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_comic()
        print("complete")
