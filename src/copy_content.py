import os
import shutil

def copy_content(src_dir, dest_dir):
    try:
        if os.path.exists(dest_dir):
            shutil.rmtree(dest_dir)
        os.mkdir(dest_dir)

        recursive_copy(src_dir, dest_dir)

    except Exception as e:
        print(e)


def recursive_copy(src_dir, dest_dir):
    src_dir_list = os.listdir(src_dir)

    for item in src_dir_list:
        src_item_path = os.path.join(src_dir, item)
        dest_item_path = os.path.join(dest_dir, item)

        if os.path.isfile(src_item_path):
            shutil.copy(src_item_path, dest_item_path)
            print(f'Copied file {item} from {src_dir} to {dest_dir}')
        else:
            os.mkdir(dest_item_path)
            print(f'Directory created at: {dest_item_path}')
            recursive_copy(src_item_path, dest_item_path)
