import arcpy
from arcpy import env

env.workspace = "P:\Data\Exercise06"

fclist = arcpy.ListFeatureClasses()

for fc in fclist:
    fcdescribe = arcpy.Describe(fc)
    print ("{} is a {} feature class".format(fcdescribe.basename,
                                             fcdescribe.shapeType))



