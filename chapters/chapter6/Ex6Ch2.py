import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "E:/School/Python/Python/Data/Exercise06"
arcpy.CreateFileGDB_management("E:/School/Python/Python/Data/Exercise06/Results", "NM.gdb")
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    if fcdesc.shapeType == 'Polygon':
        arcpy.CopyFeatures_management(fc, "E:/School/Python/Python/Data/Exercise06/Results/NM.gdb/" + fcdesc.basename)
