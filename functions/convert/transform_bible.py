# -*- coding: utf-8 -*-

# Transforms ULB or UDB from USFM to html

from __future__ import print_function, unicode_literals

import os
import shutil
import tempfile
import string
import codecs

from glob import glob
from shutil import copyfile
from general_tools.file_utils import unzip, make_dir, write_file
from general_tools.url_utils import download_file
from usfm_tools.transform import UsfmTransform

#from door43_tools.bible_handler import BibleInspection


class TransformBible(object):

    def __init__(self, source_url, output_dir, options):
        self.source_url = source_url
        self.output_dir = output_dir
        self.options = options
        self.download_dir = tempfile.mkdtemp(prefix='download_')
        self.files_dir = tempfile.mkdtemp(prefix='files_')
        self.log = []
        self.warnings = []
        self.errors = []

    def log_message(self, message):
        print(message)
        self.log.append(message)

    def error_message(self, message):
        print(message)
        self.errors.append(message)

    def warning_message(self, message):
        print(message)
        self.warnings.append(message)

    def close(self):
        # delete temp files
        if os.path.isdir(self.download_dir):
            shutil.rmtree(self.download_dir, ignore_errors=True)
        if os.path.isdir(self.files_dir):
            shutil.rmtree(self.files_dir, ignore_errors=True)

    def run(self):
        # download the archive
        file_to_download = self.source_url
        filename = self.source_url.rpartition('/')[2]
        downloaded_file = os.path.join(self.download_dir, filename)
        self.log_message('Downloading {0}...'.format(file_to_download))
        if not os.path.isfile(downloaded_file):
            try:
                download_file(file_to_download, downloaded_file)
            finally:
                if not os.path.isfile(downloaded_file):
                    raise Exception("Failed to download {0}".format(file_to_download))
                else:
                    self.log_message('Download successful.')

        # unzip the archive
        self.log_message('Unzipping {0}...'.format(downloaded_file))
        unzip(downloaded_file, self.files_dir)
        self.log_message('Unzip successful.')

        # create output directory
        make_dir(self.output_dir)

        # read the usfm files and output html files
        self.log_message('Processing the Bible USFM files')

        files = sorted(glob(os.path.join(self.files_dir, '*')))

        current_dir = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(current_dir, 'bible-template.html')) as template_file:
            html_template = string.Template(template_file.read())

        complete_html = ''
        for filename in files:
            if filename.endswith('.usfm'):
                # read the markdown file
                scratch_dir = tempfile.mkdtemp(prefix='scratch_')
                copyfile(filename, os.path.join(scratch_dir, os.path.basename(filename)))
                filebase = os.path.splitext(os.path.basename(filename))[0]
                UsfmTransform.buildSingleHtml(scratch_dir, scratch_dir, filebase)
                html_filename = filebase+".html"
                with codecs.open(os.path.join(scratch_dir, html_filename), 'r', 'utf-8-sig') as html_file:
                    html = html_file.read()
                complete_html += html
                html = html_template.safe_substitute(content=html)
                output_file = os.path.join(self.output_dir, html_filename)
                write_file(output_file, html)
                self.log_message('Converted {0} to {1}.'.format(os.path.basename(filename), os.path.basename(html_filename)))
            else:
                output_file = os.path.join(self.output_dir, os.path.basename(filename))
                copyfile(filename, output_file)

        manifest_file = os.path.join(self.files_dir, 'manifest.json')
        if os.path.isfile(manifest_file):
            copyfile(manifest_file, os.path.join(self.output_dir, 'manifest.json'))

        # Do the Bible inspection
#        inspector = BibleInspection(self.output_dir)
#        inspector.run()
#        for warning in inspector.warnings:
#            self.warning_message(warning)
#        for error in inspector.errors:
#            self.error_message(error)

#        complete_html = html_template.safe_substitute(content=complete_html)
#        write_file(os.path.join(self.output_dir, 'all.html'), complete_html)
#        self.log_message('Made one HTML of all bibles in all.html.')
#        self.log_message('Finished processing Markdown files.')
