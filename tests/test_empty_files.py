from approvaltests import verify_file

from empty_files.empty_files import create_empty_file


def test_simple():
    create_empty_file("temp/empty.txt")
    verify_file("temp/empty.txt")

