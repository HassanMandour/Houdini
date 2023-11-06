#####################
# group
import importlib, sys, os
# Append the path of the directory containing 'nodeCreator.py';
# here it's under 'C:\Users\pc\Documents\houdini19.5\scripts\myScripts'
sys.path.append(os.path.join(
    hou.getenv('HOUDINI_USER_PREF_DIR'), 'scripts', 'myscripts'))

import nodeCreator
importlib.reload(nodeCreator)


config = {
    'sop': ["groupcreate", "group"],

    'lop': ["collection::2.0", "collection"],

    'dop': ["popgroup", "group"],

    'top': ["partitionbyattribute", "partitionbyattribute"],
}

node = nodeCreator.nodeCreator(config)
if node:
    node.setColor(hou.Color(0.1843,0.5255,0.4588))
    node.setUserData("nodeshape", "slash")

#####################
# wrangle
import importlib, sys, os
sys.path.append(os.path.join(
    hou.getenv('HOUDINI_USER_PREF_DIR'), 'scripts', 'myscripts'))

import nodeCreator
importlib.reload(nodeCreator)

config = {
    'sop': ["attribwrangle","wrangle"],

    'dop': ["popwrangle", "popwrangle"]
}

node = nodeCreator.nodeCreator(config)
if node:
    color = hou.Color(0.573, 0.353, 0)
    node.setColor(color)

#####################
# split
import importlib, sys, os
sys.path.append(os.path.join(
    hou.getenv('HOUDINI_USER_PREF_DIR'), 'scripts', 'myscripts'))

import nodeCreator
importlib.reload(nodeCreator)


config = {
    'sop': ["split", "split"],
}

node = nodeCreator.nodeCreator(config)
if node:
    node.setUserData("nodeshape", "chevron_down")

    input = node.input(0)

    if input:
        # if the first input is a group node, get its groupname
        # and set as the grp to delete/keep
        if input.type().name() == 'groupcreate':
            grpname = input.parm('groupname').eval()
            node.parm('group').set(grpname)

            # if the grp name is 'keep', _personal preference_, : negate!
            if grpname.startswith('keep'):
                node.parm('negate').set(1)

#####################
# null
import importlib, sys, os
sys.path.append(os.path.join(
    hou.getenv('HOUDINI_USER_PREF_DIR'), 'scripts', 'myscripts'))

import nodeCreator
importlib.reload(nodeCreator)


config = {
    'sop': ["null", "_out"],
}

node = nodeCreator.nodeCreator(config)
if node:
    node.setColor(hou.Color(0,0,0))
    node.setUserData("nodeshape", "circle")

#####################
# blast / delete
import importlib, sys, os
sys.path.append(os.path.join(
    hou.getenv('HOUDINI_USER_PREF_DIR'), 'scripts', 'myscripts'))

import nodeCreator
importlib.reload(nodeCreator)


config = {
    'sop': ["blast", "blast"],

    'top': ["filterbyexpression", "filterbyexpression"],

    'lop': ["prune", "prune"],

    'dop': ["popkill", "popkill"]
}

node = nodeCreator.nodeCreator(config)
if node:
    node.setColor(hou.Color(0.6,0,0))
    node.setUserData("nodeshape", "star")


    input = node.input(0)
    if input:
        # if the first input is a group node, get its groupname
        # and set as the grp to delete/keep
        if input.type().name() == 'groupcreate':
            grpname = input.parm('groupname').eval()
            node.parm('group').set(grpname)

            # if the grp name is 'keep', _personal preference_, : negate!
            if grpname.startswith('keep'):
                node.parm('negate').set(1)

#####################
# copy to points
import importlib, sys, os
sys.path.append(os.path.join(
    hou.getenv('HOUDINI_USER_PREF_DIR'), 'scripts', 'myscripts'))

import nodeCreator
importlib.reload(nodeCreator)


config = {
    'sop': ["copytopoints::2.0", "copyToPoints"],

    'lop': ["instancer", "instancer"],
}

node = nodeCreator.nodeCreator(config)
