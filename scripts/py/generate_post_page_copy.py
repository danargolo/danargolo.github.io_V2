import os
import re

from format import format_header
from datetime import datetime

styles = {
    "page": 'posts',
    "class": 'post'
}

# def format_content(post):
#     print(post)
#     match_title = re.search(r'<h2>(.*?)<\/h2>', post)
#     match_content = re.compile(r'<p>(.*?)<\/p>', re.DOTALL).findall(post)

#     match_author = re.search(r'<h3>(.*?)<\/h3>',  post)

#     # print("testes", match_content)
#     # print("testes2", match_content2)

#     modified_matches = [f'<p>{match}</p>' for match in match_content]

#     print(modified_matches)



#     matches_br = match_content2[0].replace('\n', '<br>')
#     formated_paragraphs = re.sub(r'(<br>\s*){2}', '</p> <p>', matches_br)


#     # print(formated_paragraphs)
   

#     post_title = match_title.group(1) if match_title else 'No Title'
#     post_author = match_author.group(1) if match_author else 'No Author'
#     post_content = match_content.group(1) if match_content else 'No Author'

#     return(
#     f""" 
#     <h1>{post_title}</h1>
#     <p>{post_content}</p>
#     <h6>Criando por<h5>{post_author}</h5></h6>
# """
#     )

def generate_post_page(data, md):
    current_date = datetime.now()
    year_folder = current_date.strftime('%Y')
    month_folder = current_date.strftime('%m')

    folder_path = os.path.join('posts', year_folder, month_folder)
    os.makedirs(folder_path, exist_ok=True)

    file_name = f"post_{current_date.strftime('%Y%m%d_%H%M')}.html"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, 'w') as html_file:
        html_file.write(format_header(
            data['configs'],
            md,
            styles
            ))
        
    print(f'{file_name} created.')

    
