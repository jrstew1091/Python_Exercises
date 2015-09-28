import arcpy

extensions = ["3d", "Network", "Spatial", "STUFF"]
print("The following extensions are available: ")

for extension in extensions:
    if arcpy.CheckExtension(extension) == 'Available':
        print("{} Available".format(extension))
    else:
        print("{} Not Available!".format(extension))
