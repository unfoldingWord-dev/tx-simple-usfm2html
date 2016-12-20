from setuptools import setup, find_packages
from codecs import open
from os import path

setup(
    name="tx-simple-usfm2html",
    version="1.0.0",
    description="USFM-to-HTML conversion",
    long_description="USFM-to-HTML conversion",
    url="https://github.com/unfoldingWord-dev/tx-simple-usfm2html",
    author="unfoldingWord",
    author_email="info@door43.org",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
    ],
    dependency_links=[
        "git+git://github.com/unfoldingWord-dev/USFM-Tools.git#egg=usfm_tools"
    ],
    keywords=["usfm", "html"],
    packages=find_packages(),
    install_requires=["future","pyparsing","tx-shared-tools","usfm_tools"],
    test_suite="tests"
)
