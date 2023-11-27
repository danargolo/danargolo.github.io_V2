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
    f"""
        <article class="post">
            <h3><a class="post_title" href="{file_path}">{post_title}</a></h3>
            <p>{post_content[0:150]}...<br/><strong>Continue lendo
            </strong></p>
            <h5>Author: {post_author}</h5>
        </article>"""
    )

def generate_index(config):
    posts_contents = ''

    for ano in os.listdir(posts_folder):
        pasta_ano = os.path.join(posts_folder, ano)

        for mes in os.listdir(pasta_ano):
            pasta_mes = os.path.join(pasta_ano, mes)

            for post_file in reversed(sorted(os.listdir(pasta_mes))):
                if post_file.endswith('.html'):
                    post_path = os.path.join(pasta_mes, post_file)
                    posts = generate_post_link(post_path)
                    posts_contents += posts
            
    with open(template_index_path, 'r', encoding='utf-8') as template_file:
        index_content = template_file.read()
        
        index_content = index_content.format(
                title=config['title'],
                description=config['description'],
                author=config['author'],
                occupation=config['occupation'],
                github=config['links']['github'],
                linkedin=config['links']['linkedin'],
                posts_section=posts_contents
            )
        
    with open('./index.html', 'w', encoding='utf-8') as index_file:
        index_file.write(format_header(config, posts_contents))

    # print(format_header(config, posts_contents))
    print('Index created.')