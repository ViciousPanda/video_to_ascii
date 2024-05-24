import os
import shutil


def combine_path(directory, sub_directory=None, filename=None):
    root_dir = os.path.dirname(__file__)
    combined_path = os.path.join(root_dir, directory)
    if sub_directory:
        combined_path = os.path.join(combined_path, sub_directory)
    if filename:
        combined_path = os.path.join(combined_path, filename)
    return combined_path


def check_dir(directory):
    if os.path.isdir(directory):
        return True
    return False


def delete_dir(directory):
    print("removing temperary folder")
    shutil.rmtree(directory)


def make_dir(directory):
    print("making a new directory at {}".format(directory))
    os.mkdir(directory)


def make_temp_dir(directory, sub_directory):
    path = combine_path(directory, sub_directory)
    if check_dir(path):
        delete_dir(path)
    make_dir(path)
    return path
