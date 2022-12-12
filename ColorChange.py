import maya.cmds as cmds

sel= cmds.ls(sl=True)

maya.setAttr(overrideEnabled =1)
maya.setAttr(overrideRGBColors  = 8)
maya.setAttr(overideColorRGB = 1)


sels = cmds.ls(sl=True)

#maya.cmds.setAttr(curve + ".overrideEnabled", 1)
#maya.cmds.setAttr(curve + ".overrideRGBColors",1)
#maya.cmds.setAttr(curve + ".overrideColorRGB", 1 ,3 ,5)