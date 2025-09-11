import os
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def generate_page(basepath, from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    md = ''
    template = ''

    with open(from_path) as f:
        md = f.read()

    with open(template_path) as f:
        template = f.read()

    node = markdown_to_html_node(md)
    html = node.to_html()
    title = extract_title(md)
    
    
    template = template.replace('{{ Title }}', title)
    template = template.replace('{{ Content }}', html)
    template = template.replace('href="/', 'href="{basepath}')
    template = template.replace('src="/', 'src="{basepath}')

    filename = dest_path.split('/')[-1]
    template = template.replace('{{ Content }}', html)

    directory_name = dest_path.replace(f'/{filename}', '')

    os.makedirs(directory_name, exist_ok=True)

    with open(dest_path, 'w') as f:
        f.write(template)

