from logging import exception
from flask import Flask, jsonify
from flask_cors import CORS
from flask_caching import Cache
from functools import lru_cache
import requests
import json


app = Flask(__name__)
CORS(app)

PORT = 3001
HOST = '0.0.0.0'
BASE_URL  = 'https://pokeapi.co/api/v2/pokemon'
BASE_URL_IMG = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon'

config = {
  "DEBUG": True,          # some Flask specific configs
  "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
  "CACHE_DEFAULT_TIMEOUT": 3600
}

app.config.from_mapping(config)
cache = Cache(app)

@app.route('/')
def home():
  return jsonify(hello='Wellcome')

@app.route('/getall')
@cache.cached(key_prefix='all_items')
def getAll():
  try:
    # Get all pokes
    r = requests.get('{}?limit=100000&offset=0'.format(BASE_URL))
    # Check base URL
    if r.status_code != 200:
      raise Exception('Don\'t get items of BASE_URL')
    # Check items in results
    items = json.loads(r.content).get('results')
    if len(items) == 0:
      raise Exception('Don\'t items in results')
    # Check info in the url of first item
    r2 = requests.get(items[0].get('url'))
    if r2.status_code != 200:
      raise Exception('Don\'t item don\'t url')
    # Get url of image or string default
    url_img_api = json.loads(r2.content).get('sprites').get('front_default') or 'string_of_escape_to_empty'
    # Check base_url_img vs url_img from api
    if url_img_api.find(BASE_URL_IMG) == -1:
      raise Exception("The base url of images has been changed")
    parseItems = []
    for item in items:
      id = item.get('url').split('/').pop(-2)
      img = "{url_img}/{id}.png".format(url_img=BASE_URL_IMG, id=id)
      parseItems.append({
        "name": item.get('name'),
        "img": img
      })
    return jsonify(parseItems)
  except Exception as err:
    message = '[In get all]: {}'.format(err)
    return jsonify(error=message)

@app.route('/search/<name>')
@lru_cache()
def filter(name):
  r = getAll()
  items = json.loads(r.data)
  return jsonify([x for x in items if x.get('name').find(name) != -1])


if __name__ == '__main__':
  app.run(host=HOST, port=PORT)
  print('Server running in port %s' %(PORT))




