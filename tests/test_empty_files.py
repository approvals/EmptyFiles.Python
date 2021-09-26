import os
import shutil

from approvaltests import verify_file

from empty_files.empty_files import create_empty_file


def test_create_base_empty_file():
    verify_file_creation("temp/empty.txt")


def verify_file_creation(file_name):
    clear_temp()
    create_empty_file(file_name)
    verify_file(file_name)


def test_create_empty_file_in_nested_directory():
    verify_file_creation("temp/temp/empty.txt")


def clear_temp():
    if os.path.exists("temp"):
        shutil.rmtree("temp")

