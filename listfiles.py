import nuke
import glob

path = '/Users/gui/Dropbox/0000_ELIS/Figurantes/'

arqs = glob.glob(path+'*')

for node in nuke.selectedNodes():
    if node.Class() != 'Read':
        continue
    print node['file'].value()

