import os
from generate_index import generate_index
from datetime import datetime

def generate_post_page(post):
    with open('templates/template_post.html', 'r') as template_file:
        template_content = template_file.read()

    current_date = datetime.now()
    year_folder = current_date.strftime('%Y')
    month_folder = current_date.strftime('%m')

    folder_path = os.path.join('posts', year_folder, month_folder)
    os.makedirs(folder_path, exist_ok=True)

    file_name = f"post_{current_date.strftime('%Y%m%d_%H%M')}.html"
    file_path = os.path.join(folder_path, file_name)

    template_content = template_content.format(
        post_title=post['title'],
        post_content=post['content'],
        date_time=current_date.strftime('%a %d %m %Y, %I:%M%p'),
        post_author=post['author']
        )

    with open(file_path, 'w') as html_file:
        html_file.write(template_content)
    print(f'{file_name} created.')
    
