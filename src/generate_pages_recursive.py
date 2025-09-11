import os
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def generate_pages_recursive(basepath, from_path, template_path, dest_path):

    directory_list = os.listdir(from_path)
    
    for item in directory_list:
        new_from_path = os.path.join(from_path, item)
        new_dest_path = os.path.join(dest_path, item)

        if '.md' in item:
            print(f'Generating page from {new_from_path} to {new_dest_path} using {template_path}')

            md = ''
            template = ''

            with open(new_from_path) as f:
                md = f.read()

            with open(template_path) as f:
                template = f.read()

            node = markdown_to_html_node(md)
            html = node.to_html()
            title = extract_title(md)

            template = template.replace('{{ Title }}', title)
            template = template.replace('{{ Content }}', html)
            template = template.replace('href="/', f'href="{basepath}')
            template = template.replace('src="/', f'src="{basepath}')
            filename = new_dest_path.split('/')[-1]

            filename_html = filename.replace('.md', '.html')

            directory_name = new_dest_path.replace(f'/{filename}', '')
            os.makedirs(directory_name, exist_ok=True)

            new_dest_path_html = os.path.join(directory_name, filename_html)

            with open(new_dest_path_html, 'w') as f:
                f.write(template)
        
        elif not os.path.isfile(item):
            os.mkdir(new_dest_path)
            generate_pages_recursive(basepath, new_from_path, template_path, new_dest_path)
