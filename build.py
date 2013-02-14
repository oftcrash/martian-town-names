# Author: Kris Knowlton
# Copyright: 2013 Kris Knowlton. This work is licensed under the Creative Commons Attribution 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by/3.0/ or send a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.

from settings import *

#pass the grf name as an argument, or ask for a name if the argument isn't passed
try:
	script, name = argv
except:
	print 'Enter a grf name:',
	name = raw_input()

#get the current build number
def getBuildNumber():
	if os.path.isfile(buildCount):
		try:
			file = open(buildCount)
			build = int(file.readline())
			file.close()
		except IOError as e:
			build = 1
	else:
		build = 1
	return build

#set the version by advancing the build by 1
def setVersion():
	build = getBuildNumber() + 1
	ver = str(build)
	file = open(buildCount, 'w')
	file.write(ver)
	file.close()
	return ver

#build the custom_tags file
def customTags():
	version = setVersion()
	ct = open(os.path.join(buildPath, 'custom_tags.txt'), 'w')
	ct.write('VERSION:' + version + '\n')
	ct.write('UPDATEDT:' + str(datetime.now()) + '\n')
	ct.write('TITLE:Martian Town Names 1.0\n')
	ct.write('AUTHOR:Kris Knowlton\n')
	ct.write('COPYRIGHTDT:2013\n')
	ct.write('LICENSE:CC by 3.0\n')
	ct.close()
	print 'created custom_tag.txt'

#copy any lang files from source to the build.
def lang():
	source = os.path.join(sourcePath, 'lang')
	dest = os.path.join(buildPath, 'lang')
	lngFiles = os.listdir(source)
	for lngFile in lngFiles:
		fileName = os.path.join(source, lngFile)
		if (os.path.isfile(fileName)):
			shutil.copy(fileName, dest)
			print 'copied ' + lngFile
		
#write the nml file
def writeNML(content):
	try:
		dest = os.path.join(buildPath, name + '.nml')
		nml = open(dest, 'a')
		nml.write(content)
		nml.close()
	except Exception as e:
		print e

#set up the build directory
def setupBuild():
	subdirs = ['gfx','lang']
	if not os.path.exists(buildPath):
		os.makedirs(buildPath)
		for s in subdirs:
			os.makedirs(os.path.join(buildPath, s))
			print 'created %s directory' % s

#archive any existing builds before starting a new one
def cleanup():
	if os.path.exists(buildPath):
		if not os.path.exists(archivePath):
			os.makedirs(archivePath)
			print '  created archive directory'
		build = str(getBuildNumber())
		os.rename(buildPath, os.path.join(archivePath, build))
		print '  archived build %s' % build

def readCSV():
	env = Environment(loader=FileSystemLoader(templatePath), trim_blocks=True)
	out = ''
	reader = csv.reader(open('mars_names.csv', 'rU'))
	out += env.get_template('grf.tnml').render(version = getBuildNumber())
	real_names = []
	root_names = []
	prefixes = []
	suffixes = []
	for row in reader:
		if row[0]:
			real_names.append(row[0])
		if row[1]:
			root_names.append(row[1])
		if row[2]:
			prefixes.append(row[2] + ' ')
		if row[3]:
			suffixes.append(' ' + row[3])
	out += env.get_template('town_names.tnml').render(id='real_names', names=real_names)
	out += env.get_template('town_names.tnml').render(id='prefixes', names=prefixes)
	out += env.get_template('town_names.tnml').render(id='suffixes', names=suffixes)
	out += env.get_template('town_names.tnml').render(id='root_names', names=root_names)
	out += '''
	town_names(root_suf) {
		{
			town_names(root_names,1)
		}
		{
			town_names(suffixes,1)
		}
	}
	town_names(pre_root) {
		{
			town_names(prefixes,1)
		}
		{
			town_names(root_names,1)
		}
	}
	town_names(base_names) {
		styles:	string(STR_GAME_OPTIONS_TOWN_NAME_MARS);
		{
			town_names(real_names,1),
			town_names(root_names,3),
			town_names(pre_root,1),
			town_names(root_suf,15),
		}
	}
	'''
	return out

#create the new build
def newBuild():
	print 'Starting build...'
	print 'Clean up:'
	cleanup()
	print 'Set up build:'
	setupBuild()
	customTags()
	lang()
	writeNML(readCSV())
	try:
		os.chdir(buildPath)
		os.system('nmlc ' +  name + '.nml')
		newgrfFile = name + '.grf'
		print 'compiled %s' % newgrfFile
	except:
		print 'error compiling'
	else:
		if os.path.isfile(newgrfFile):
			os.system('mv %s %s' % (newgrfFile,newgrfPath))
			print 'copied %s to %s' % (newgrfFile,newgrfPath)
			print 'SUCCESS!'


newBuild()