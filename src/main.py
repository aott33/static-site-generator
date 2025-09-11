import sys
from copy_content import copy_content
from generate_pages_recursive import generate_pages_recursive

def main():
    basepath = '/'
    if len(sys.argv) >= 2:
        basepath = sys.argv[1]

    src_dir = '/home/ubuntu/static-site-generator/static'
    dest_dir = '/home/ubuntu/static-site-generator/docs'
    copy_content(src_dir, dest_dir)

    from_path = '/home/ubuntu/static-site-generator/content'
    template_path = '/home/ubuntu/static-site-generator/template.html'
    dest_path = '/home/ubuntu/static-site-generator/docs'
    generate_pages_recursive(basepath, from_path, template_path, dest_path)

if __name__ == "__main__":
    main()

