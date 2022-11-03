import maya.cmds as cmds

cmds.polyCube(height=3, width=3, depth=3, subdivisionsZ=2, subdivisionsX=2)
cmds.move(-1.450, moveX=True)


cmds.polyCylinder(r=.5, h=.25)
cmds.move(1.5633540, moveY=True, a=True)
cmds.move(-.74, moveX=True)
cmds.move(-0.89, moveZ=True)

cmds.polyCylinder(r=.5, h=.25)
cmds.move(1.5633540, moveY=True, a=True)
cmds.move(-.74, moveX=True)
cmds.move(0.771, moveZ=True)

cmds.polyCylinder(r=.5, h=.25)
cmds.move(1.5633540, moveY=True, a=True)
cmds.move(-2.3, moveX=True)
cmds.move(0.771, moveZ=True)

cmds.polyCylinder(r=.5, h=.25)
cmds.move(1.5633540, moveY=True, a=True)
cmds.move(-2.3, moveX=True)
cmds.move(-0.89, moveZ=True)