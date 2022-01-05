import maya.cmds as cmds

cir01 = cmds.circle(nr = [0,1,0],ch=0)
cir02 = cmds.circle(nr = [1,0,0],ch=0)
cir03 = cmds.circle(nr = [0,0,1],ch=0)

cir01Shape = cmds.listRelatives(cir01, s = True)
cir02Shape = cmds.listRelatives(cir02, s = True)
cir03Shape = cmds.listRelatives(cir03, s = True)


cmds.parent(cir02Shape,cir03Shape,cir01, r=True, shape =True)
cmds.delete(cir02,cir03)
cmds.rename(cir01,"spl_Ctrl")
cmds.select(cl=1)
