# Name: AddXY_Example2.py
# Description: Adding XY points to the climate dataset

# Import system modules
import arcpy
from arcpy import env

# Set workspace
env.workspace = "P:\Python_Exercises\Data\Exercise05"

# Set local variables
in_data= "hospitals.shp"
in_features = "hospitalsXYpts.shp"

# Copying data to preserve original dataset
# Execute Copy
arcpy.Copy_management("hospitals.shp", "hospitalsXYpts.shp")

# Execute AddXY
arcpy.AddXY_management("hospitalsXYpts.shp") 
