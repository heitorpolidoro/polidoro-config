import contextlib
import os


@contextlib.contextmanager
def change_dir(destination):
    orig_dir = os.getcwd()
    os.chdir(destination)
    yield
    os.chdir(orig_dir)
