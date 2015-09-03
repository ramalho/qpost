import nuke
import glob
import ramautil

path = '/Users/gui/Dropbox/0000_ELIS/Figurantes/'

arqs = glob.glob(path+'*')

pics = ramautil.endless_shuffle(arqs)

for node, pic in zip(nuke.selectedNodes('Read'), pics):
    print node['file'].setValue(pic)
