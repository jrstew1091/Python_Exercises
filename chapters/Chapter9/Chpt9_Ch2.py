import arcpy
from arcpy import env
env.workspace = "C:/Python/Data/Exercise09"

arcpy.CreateFileGDB_management("C:/Python/Data/Exercise09/Results", "Challenge2")

Input_Rasters = arcpy.ListRasters()
for raster in Input_Rasters:
    arcpy.RasterToGeodatabase_conversion(raster, "C:/Python/Data/Exercise09/Results/Challenge2.gdb")
