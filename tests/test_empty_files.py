import os
import shutil
from pathlib import Path

from approvaltests import verify_file, Options

from empty_files.empty_files import create_empty_file


def test_create_base_empty_file():
    verify_file_creation("temp/empty.txt")

def test_create_binary():
    verify_file_creation("temp/empty.jpg")


def test_create_empty_file_in_nested_directory():
    verify_file_creation("temp/temp/empty.txt")


def verify_file_creation(file_name):
    clear_temp()
    create_empty_file(file_name)
    extension = Path(file_name).suffixes[0]

    verify_file(file_name, options=Options().for_file.with_extension(extension))


def clear_temp():
    if os.path.exists("temp"):
        shutil.rmtree("temp")

