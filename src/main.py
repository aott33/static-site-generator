from copy_content import copy_content
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive

def main():
    src_dir = '/home/ubuntu/static-site-generator/static'
    dest_dir = '/home/ubuntu/static-site-generator/public'
    copy_content(src_dir, dest_dir)

    from_path = '/home/ubuntu/static-site-generator/content'
    template_path = '/home/ubuntu/static-site-generator/template.html'
    dest_path = '/home/ubuntu/static-site-generator/public'
    generate_pages_recursive(from_path, template_path, dest_path)

#    from_path = '/home/ubuntu/static-site-generator/content'
#    template_path = '/home/ubuntu/static-site-generator/template.html'
#    dest_path = '/home/ubuntu/static-site-generator/public'
#    generate_page(from_path, template_path, dest_path)
#
#    from_path = '/home/ubuntu/static-site-generator/content/blog/glorfindel/index.md'
#    template_path = '/home/ubuntu/static-site-generator/template.html'
#    dest_path = '/home/ubuntu/static-site-generator/public/blog/glorfindel/index.html'
#    generate_page(from_path, template_path, dest_path)
#
#    from_path = '/home/ubuntu/static-site-generator/content/blog/tom/index.md'
#    template_path = '/home/ubuntu/static-site-generator/template.html'
#    dest_path = '/home/ubuntu/static-site-generator/public/blog/tom/index.html'
#    generate_page(from_path, template_path, dest_path)
#    
#    from_path = '/home/ubuntu/static-site-generator/content/blog/majesty/index.md'
#    template_path = '/home/ubuntu/static-site-generator/template.html'
#    dest_path = '/home/ubuntu/static-site-generator/public/blog/majesty/index.html'
#    generate_page(from_path, template_path, dest_path)
# 
#    from_path = '/home/ubuntu/static-site-generator/content/contact/index.md'
#    template_path = '/home/ubuntu/static-site-generator/template.html'
#    dest_path = '/home/ubuntu/static-site-generator/public/contact/index.html'
#    generate_page(from_path, template_path, dest_path)

if __name__ == "__main__":
    main()

