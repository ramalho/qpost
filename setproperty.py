import nuke

for node in nuke.selectedNodes('Read'):
    node['postage_stamp'].setValue(1)
