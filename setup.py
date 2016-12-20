from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


with open(path.join(here, "README.md"), "r") as f:
    long_description = f.read()

setup(
    name="tx-simple-usfm2html",
    version="1.0.0",
    description="USFM-to-HTML conversion",
    long_description=long_description,
    url="https://github.com/unfoldingWord-dev/tx-simple-usfm2html",
    author="unfoldingWord",
    author_email="info@door43.org",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
    ],
    keywords=["usfm", "html"],
    packages=find_packages(),
    install_requires=["future"],
    test_suite="tests"
)
