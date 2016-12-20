import os
from setuptools import setup
from setuptools.command.install import install


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(f_name):
    return open(os.path.join(os.path.dirname(__file__), f_name)).read()

setup(
    name="tx-simple-usfm2html",
    version="1.0.0",
    author="unfoldingWord",
    author_email="unfoldingword.org",
    description="Lambda function to conver USFM to HTML",
    license="MIT",
    keywords="unfoldingWord publish",
    url="https://github.org/unfoldingWord-dev/tx-simple-usfm2html",
    long_description=read('README.md'),
    classifiers=[],
    dependency_links=[
        'git+git://github.com/unfoldingWord-dev/uw_tools.git#egg=uw_tools',
    ],
    install_requires=[
        'markdown',
        'requests',
        'uw_tools'
    ],
    test_suite='tests',
)
