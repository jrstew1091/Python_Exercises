import arcpy

arcpy.env.workspace = "c:/Python/Data/Exercise07/"

arcpy.AddField_management("c:/Python/Data/Exercise07/Results/roads.shp", "FERRY", "TEXT",)

cursor = arcpy.da.UpdateCursor("c:/Python/Data/Exercise07/Results/roads.shp", ['FEATURE', 'FERRY'])

for row in cursor:
    if row[0] == 'Ferry Crossing':
        row[1] = 'Yes'
    else:
        row[1] = 'No'

    cursor.updateRow(row)
