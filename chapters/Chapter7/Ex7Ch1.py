import arcpy

arcpy.env.workspace = "c:/python/data/exercise07/"

unique_name = arcpy.CreateUniqueName("Results/airportsforbuf.shp")
arcpy.Select_analysis("c:/python/data/exercise07/airports.shp", unique_name, """"FEATURE" = 'Airport'""")

unique_name = arcpy.CreateUniqueName("Results/seaplaneforbuf.shp")
arcpy.Select_analysis("c:/python/data/exercise07/airports.shp", unique_name, """"FEATURE" = 'Seaplane Base'""")

unique_name = arcpy.CreateUniqueName("Results/buffer_airports.shp")
arcpy.Buffer_analysis("c:/python/data/exercise07/results/airportsforbuf.shp", unique_name, "15000 METERS")

unique_name = arcpy.CreateUniqueName("Results/buffer_seaplanebase.shp")
arcpy.Buffer_analysis("c:/python/data/exercise07/results/seaplaneforbuf.shp", unique_name, "7500 METERS")
