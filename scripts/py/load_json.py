#!/usr/bin/env python3

import json
from markdown2 import markdown

from generate_post_page_copy import generate_post_page
from generate_index_copy import generate_index

def load_json():
  data = {}
  with open('post_blog.md') as md_file:
      md_content = markdown(
         md_file.read(),
         extras=['fenced-code-blocks', 'code-friendly']
      )
      # print(md_content)

  # with open('post_data.json', 'r') as json_file:
  #     json_data = json.load(json_file)
  #   #   print('JSON loaded.')
  
  with open('config_blog.json', 'r') as config_file:
      config_data = json.load(config_file)

      data['configs'] = config_data

    #   print(data)
  
  generate_post_page(data, md_content)

  generate_index(data)

load_json() 