import os
import re
from format import format_header

posts_folder = './posts'
template_index_path = './templates/index.html'

def generate_post_link(file_path):
    with open(file_path, 'r', encoding='utf-8') as post_file:
        file_content = post_file.read()

    match_title = re.search(r'<h1>(.*?)<\/h1>', file_content)
    match_content = re.search(r'<p>(.*?)<\/p>', file_content, re.DOTALL)
    match_author = re.search(r'<h5>(.*?)<\/h5>', file_content)

    post_title = match_title.group(1) if match_title else 'No Title'
    post_content = match_content.group(1) if match_content else 'No Content'
    post_author = match_author.group(1) if match_author else 'No Author'

    return (
    f"""<article class="post">
        <a class="post_title" href="{file_path}"><h3>{post_title}</h3></a>
        <a href="{file_path}"><p>{post_content[0:150]}...<br/><strong>Continue lendo
        </strong></a></p>
        <h5>Author: {post_author}</h5>
      </article>
      """)

def generate_index(config):
    posts_contents = ''

    for year in os.listdir(posts_folder):
        folder_year = os.path.join(posts_folder, year)

        for month in os.listdir(folder_year):
            folder_month = os.path.join(folder_year, month)

            for post_file in reversed(sorted(os.listdir(folder_month))):
                if post_file.endswith('.html'):
                    post_path = os.path.join(folder_month, post_file)
                    posts = generate_post_link(post_path)
                    posts_contents += posts
        
    with open('./index.html', 'w', encoding='utf-8') as index_file:
        index_file.write(format_header(config['configs'], posts_contents))

    print('Index created.')