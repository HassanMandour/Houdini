import hou, sys

####
net_editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)

desktop = hou.ui.curDesktop()
pane = desktop.paneTabUnderCursor()

cursorpos = pane.cursorPosition()

currentContext = pane.pwd().type().childTypeCategory().name().lower()

####

def indexByNode(node, input):
    for i, n in enumerate(node.inputs()):
        if n == input:
            return i
            break
    return -1

###
#
def nodeCreator(config: dict, preconfignode=None):
    global currentContext
    if currentContext not in config:
        currentContext = 'sop'  # Use the 'geo' definition as the fall back
                                #(e.g. 'null' node has the same definition is sops, tops, lops,, etc),
                                # we fall back to avoid repetition in 'config' dictionary therefore.

    sel = hou.selectedNodes()

    data = config[currentContext]
    nodetype = data[0]
    name = data[1]

    try:
        isApplicable = sel[0].position().isAlmostEqual(cursorpos, tolerance = 10)
    except:
        isApplicable = 0


    if isApplicable:
        sel = sel[0]
        try:
            node = sel.createOutputNode(nodetype, name)
            if callable(preconfignode):
                preconfignode(node)
        except:
            hou.ui.displayMessage(
                    'Cannot create node: incompatible pane network type')
            sys.exit(0)

        outputs = sel.outputs()
        if len(outputs) > 0:
            for output in outputs:
                if output == node:
                    continue
                output.setInput(indexByNode(output, sel), node)


        node.moveToGoodPosition()

        if(pane.pwd().type().name() == 'geo'):
            node.setDisplayFlag(1)
            node.setRenderFlag(1)

            # if sel.isRenderFlagSet():
            #     node.setRenderFlag(1)

    else:
        try:
            node = pane.pwd().createNode(nodetype, name)
            node.setPosition(cursorpos)
        except:
            hou.ui.displayMessage(
                    'Cannot create node: incompatible pane network type')
            sys.exit(0)


    node.setCurrent(1, clear_all_selected=True)

    return node

