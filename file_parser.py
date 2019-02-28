import os
dir_name = os.path.dirname(__file__)


def read_file(file_name):
    """
    Read a file and returns a list containing the lines of the file removing
    :param file_name: The relative path of the file to read
    :return: String list containing the lines of the file
    """
    file_name = os.path.join(dir_name, file_name)
    with open(file_name) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def write_file(file_name):
    """
    Create a file and returns the reference of it
    :param file_name: The relative path of the file to be created
    :return: The reference of the created file
    """
    file_name = os.path.join(dir_name, file_name)
    file = open(file_name, "w+")
    return file
