import json
from generate_post_page import generate_post_page

def load_json():
  with open('content/post_data.json', 'r') as json_file:
        json_data = json.load(json_file)
        print('JSON loaded.')
  
  generate_post_page(json_data['post'])

load_json() 