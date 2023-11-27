#!/usr/bin/env python3

import json
import markdown
from generate_post_page_copy import generate_post_page
from generate_index_copy import generate_index

def load_json():
  data = {}
  with open('post_blog.md', 'r') as md_file:
      md_content = md_file.read()
      md_data = markdown.markdown(md_content)
    #   print(md_data)

  with open('post_data.json', 'r') as json_file:
      json_data = json.load(json_file)
    #   print('JSON loaded.')
  
  with open('config_blog.json', 'r') as config_file:
      config_data = json.load(config_file)

      data['configs'] = config_data
      data['content'] = md_data

    #   print(data)
  
  generate_post_page(data)

  generate_index(data)

load_json() 