import os, sys


def app_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(os.path.abspath(sys.executable))
    else:
        return os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':
    print(app_path())
