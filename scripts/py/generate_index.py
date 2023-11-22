import os
import re

posts_folder = './posts'
template_path = './templates/index.html'

with open(template_path, 'r', encoding='utf-8') as template_file:
    index_content = template_file.read()


def generate_post_link(file_path):
    with open(file_path, 'r', encoding='utf-8') as post_file:
        file_content = post_file.read()

    match_title = re.search(r'<h1>(.*?)<\/h1>', file_content)
    match_content = re.search(r'<p>(.*?)<\/p>', file_content)
    match_author = re.search(r'<h6>(.*?)<\/h6>', file_content)

    post_title = match_title.group(1) if match_title else 'No Title'
    post_content = match_content.group(1) if match_content else 'No Content'
    post_author = match_author.group(1) if match_author else 'No Author'

    return (
        f"""  <article>
        <a id="title" href="{file_path}"><h3>{post_title}</h3></a>
        <p>{post_content}.<a href="{file_path}">Continue lendo</a></p>
        <h6>{post_author}</h6>
      </article><br/>      
    """
    )

def generate_index():
    posts_contents = ''
    index_new = ''

    for ano in os.listdir(posts_folder):
        pasta_ano = os.path.join(posts_folder, ano)

        for mes in os.listdir(pasta_ano):
            pasta_mes = os.path.join(pasta_ano, mes)

            for post_file in reversed(sorted(os.listdir(pasta_mes))):
                if post_file.endswith('.html'):
                    post_path = os.path.join(pasta_mes, post_file)
                    posts = generate_post_link(post_path)
                    posts_contents = posts_contents + posts

            initial_pos = index_content.find('id="posts">')
            first_half = index_content[0:initial_pos + len('<main id="main">')]

            final_pos = index_content.find('</section>')
            last_half = index_content[final_pos:]
            
            index_new = index_new + first_half + posts_contents + last_half

            with open('./index.html', 'w', encoding='utf-8') as index_file:
                index_file.write(index_new)

    print('Index created.')