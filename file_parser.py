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
    print(content)
    return content
