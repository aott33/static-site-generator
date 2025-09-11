from copy_content import copy_content
from generate_page import generate_page

def main():
    src_dir = '/home/ubuntu/static-site-generator/static'
    dest_dir = '/home/ubuntu/static-site-generator/public'
    copy_content(src_dir, dest_dir)

    from_path = '/home/ubuntu/static-site-generator/content/index.md'
    template_path = '/home/ubuntu/static-site-generator/template.html'
    dest_path = '/home/ubuntu/static-site-generator/public/index.html'
    generate_page(from_path, template_path, dest_path)

if __name__ == "__main__":
    main()
