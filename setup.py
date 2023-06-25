import re
from pathlib import Path

from setuptools import setup, find_packages #type: ignore

HERE = Path(__file__).parent
_version_file_contents = (HERE / "empty_files" / "version.py").read_text()
matched = re.search(r'"(.*)"', _version_file_contents)
VERSION = matched.group(1) if matched is not None else "UNKNOWN VERSION"

setup(
    name="empty-files",
    version=VERSION,
    description="Serves empty files of many types",
    author="empty_files Contributors",
    url="https://github.com/approvals/EmptyFiles.Python",
    python_requires=">=3.7.1",
    install_requires=["requests"],
    packages=find_packages(exclude=["tests*"]),
    long_description=(HERE / "README.md").read_text(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)
