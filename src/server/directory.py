import os

root = os.path.split(__file__)[0]


def get(path):
    return os.path.join(root, path)
