import os
from sys import argv #accept arguments passed from the command line
from datetime import datetime #formatting timecodes
import shutil
import json
from pprint import pprint
from jinja2 import Environment, FileSystemLoader
import csv


projectName = 'martian-town-names'
basePath = os.getcwd()
newgrfPath = os.path.join('/Users/knowltk/Documents/OpenTTD/', 'newgrf')
projectPath = basePath
buildPath = os.path.join(projectPath, 'build')
releasePath = os.path.join(projectPath, 'release')
templatePath = os.path.join(projectPath, 'templates')
sourcePath = os.path.join(projectPath, '.')
archivePath = os.path.join(projectPath, 'archive')
buildCount = 'buildcount.txt'
