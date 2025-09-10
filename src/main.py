from copy_content import copy_content

def main():
    src_dir = '/home/ubuntu/static-site-generator/static'
    dest_dir = '/home/ubuntu/static-site-generator/public'
    copy_content(src_dir, dest_dir)

if __name__ == "__main__":
    main()
