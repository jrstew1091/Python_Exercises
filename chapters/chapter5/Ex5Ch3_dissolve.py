# Name: Dissolve_Example2.py
# Description: Dissolve features based on common attributes

 
# Import system modules
import arcpy

arcpy.env.workspace = "P:/Python_Exercises/Data/Exercise05"
 
arcpy.Dissolve_management("parks.shp", "P:/Python_Exercises/Data/Exercise05/parks_dissolve.shp","PARK_TYPE", "", "SINGLE_PART", "")

