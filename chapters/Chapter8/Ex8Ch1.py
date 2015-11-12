import arcpy
import fileinput
import string
import os
from arcpy import env
env.workspace = "C:/Python/Data/Exercise08"
env.overwriteOutput = True
outpath = "C:/Python/Data/Exercise08"
newfc = "Results/newpolygon.shp"
arcpy.CreateFeatureclass_management(outpath, newfc, "Polygon")
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
coords = [[0, 0], [0, 1000], [1000, 1000], [1000, 0], [0, 0]]
for coord in coords:
    X, Y = coord
    array.add(arcpy.Point(X, Y))
cursor.insertRow([arcpy.Polygon(array)])
del cursor
