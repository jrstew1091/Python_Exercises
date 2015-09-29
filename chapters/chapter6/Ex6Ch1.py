import arcpy
from arcpy import env

env.workspace = "E:/School/Python/Python/Data/Exercise06"

fclist = arcpy.ListFeatureClasses()

for fc in fclist:
    fcdescribe = arcpy.Describe(fc)
    print ("{} is a {} feature class".format(fcdescribe.basename,
                                             fcdescribe.shapeType))



