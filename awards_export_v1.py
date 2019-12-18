
try:
    import arcpy, sys, traceback
    print "Working..."  
      
    mxdPath = r"G:\ARMAP_MapBook\ARMAP_Mapbook_v2.mxd"  
    mxd = arcpy.mapping.MapDocument(mxdPath)  
      
    df = arcpy.mapping.ListDataFrames(mxd)[0]  
    lyr = arcpy.mapping.ListLayers(mxd, "Research_ResearchSites_EPSG3572_20160715b", df)[0]  
    print lyr.dataSource  
    theAttribute = "Award_info"  
    #GetAListOfEachAttribute  
    awards = []
    print "Start cursor"  
    rows = arcpy.SearchCursor(lyr.dataSource)  
    for row in rows:  
        awards.append(row.getValue(theAttribute))
    awards_cleaned = list(set(awards))    
                                                             
      
    for item in awards_cleaned:  
        #award_query = "\""  + theAttribute + "\" = " + "'" + item + "'"  
        award_query = '"Award_Info" =' + '\''+ item + '\''  
        print  "Working on: ",item  
        print award_query  
        lyr.definitionQuery = award_query  
    
        outputjpg = "G:\ARMAP_MapBook\Maps_Export\\" + item + ".jpg"  
        arcpy.RefreshActiveView()  
        arcpy.mapping.ExportToJPEG (mxd, outputjpg)  
    print "done"  
except arcpy.ExecuteError:   
    msgs = arcpy.GetMessages(2)   
    arcpy.AddError(msgs)    
#If the error is with the script, or with python, find error and report it to the screen...  
except:  
    tb = sys.exc_info()[2]  
    tbinfo = traceback.format_tb(tb)[0]  
    pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])  
    msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"  
    arcpy.AddError(pymsg)  
    arcpy.AddError(msgs)  
