import os
from sys import argv #accept arguments passed from the command line
from datetime import datetime #formatting timecodes
import shutil
import json
from pprint import pprint
from jinja2 import Environment, FileSystemLoader
import csv


projectName = 'martian_names'
basePath = '/Users/knowltk/Documents/OpenTTD/'
newgrfPath = os.path.join(basePath, 'newgrf')
projectPath = os.path.join(basePath, 'NML', 'projects', projectName)
buildPath = os.path.join(projectPath, 'build')
templatePath = os.path.join(projectPath, 'templates')
sourcePath = os.path.join(projectPath, '.')
archivePath = os.path.join(projectPath, 'archive')
buildCount = 'buildcount.txt'
