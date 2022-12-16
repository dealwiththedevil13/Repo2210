import maya.cmds as cmds


def Sequential_Renamer(string):
    Select = cmds.ls(sl=True)
    #The use of partition was a suggestion by Tanner King. Partitiion is used to create, query or add/remove sets to a partition. If a partition name needs to be specified, it is the first argument, other arguments represent the set names.#
    string.partition("##")
    for objNum, object in enumerate(Select):
        cmds.rename(object,string.partition('#')[0] + str(objNum + 1).zfill(string.count('#')) + string.rpartition('#')[2])
    #for count, object in enumerate(Select)
       # suffix = '_Jnt'
       # x = str(1).xfill(0)
   #txt = "Leg_##_JNT"
    #count = txt.count("#")

    #if x >0:
       # x = txt.find("#" * count)


Sequential_Renamer("Arm_###_jnt")



