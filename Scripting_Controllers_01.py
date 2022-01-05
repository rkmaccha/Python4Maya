import maya.cmds as cmds

selList = cmds.ls(selection=1)

mainParent = selList[0]
selList.remove(selList[0])
selListShape = []

for sel in selList:
    sShape= cmds.listRelatives(sel, s=1)[0]
    selListShape.append(sShape)

cmds.parent(selListShape,mainParent, s=True,r=True)
cmds.delete(selList)
cmds.select(cl=1)
cmds.xform(mainParent, cp=True)
