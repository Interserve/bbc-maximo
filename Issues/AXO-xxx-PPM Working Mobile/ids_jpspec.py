from psdi.server import MXServer
from psdi.security import UserInfo
from psdi.mbo import MboConstants 
from psdi.mbo import MboServerInterface
from psdi.mbo import MboRemote
from psdi.mbo import MboSetRemote


mxServer = MXServer.getMXServer()
user = mxServer.getUserInfo('TIMMINSA')
csMboSet = mxServer.getMboSet("CLASSSTRUCTURE",user )
csMboSet.setWhere("classificationid = 'JOBPLAN'")
csMboSet.reset()


if csMboSet.count() > 0:
    csMbo = csMboSet.getMbo(0)
    csID = csMbo.getString("CLASSSTRUCTUREID")
    print "##INFO## Class structure ID is: "+ csID

    ## Getting Valid Planned + Statutory Jobplans

    jpMboSet = mxServer.getMboSet("JOBPLAN",user )
    jpMboSet.setWhere("templatetype <> 'REACTIVE' and jpnum <> 'BBCMTR01'")
    jpMboSet.reset()
    print "##INFO## Job Plans: "+ str(jpMboSet .count())
    
    for a in range(jpMboSet .count()):
        jpMbo = jpMboSet.getMbo(a)
        jpMbo.setValue("CLASSSTRUCTUREID",csID,MboConstants.NOACCESSCHECK)
    
    jpMboSet.save()

    for b in range(jpMboSet .count()):
        jpMbo = jpMboSet.getMbo(b)
        jpDesc = jpMbo.getString("DESCRIPTION")
        
        ##Cleanse Data  

        if jpDesc == "CW WATER LOG (1YR)":
            jpDesc = "CW WATER LOG (1Y)"
            jpMbo.setValue("DESCRIPTION",jpDesc ,MboConstants.NOACCESSCHECK)
        if jpDesc == "SMOKE DETECTIONS SYSTEMS (Y)":
            jpDesc = "SMOKE DETECTIONS SYSTEMS (1Y)"
            jpMbo.setValue("DESCRIPTION",jpDesc ,MboConstants.NOACCESSCHECK)
        if jpDesc == "SMOKE EXTRACTION SYSTEMS (Y)":
            jpDesc = "SMOKE EXTRACTION SYSTEMS (1Y)"
            jpMbo.setValue("DESCRIPTION",jpDesc ,MboConstants.NOACCESSCHECK)



##Get Description + Duration + Unit of Measure
        if jpDesc[len(jpDesc)-3:len(jpDesc)-2] =="0":
             dur = "10"
        else:
            dur = jpDesc[len(jpDesc)-3:len(jpDesc)-2]

        uom = jpDesc[len(jpDesc)-2:len(jpDesc)-1]

##Translate UOM
        if uom == "D":
            uom = "DAILY"
        if uom == "W":
            uom = "WEEKLY"
        if uom == "M":
            uom = "MONTHLY"
        if uom == "Y":
            uom = "YEARLY"

        print jpMbo.getString("JPNUM") + ":" + jpDesc + " - " + dur + " - " + uom
 
        jpSpecMboSet = jpMbo.getMboSet("JOBPLANSPECCLASS")
        if jpSpecMboSet.count() >  0:
            jpSpecMbo = jpSpecMboSet.getMbo(0)
            print "Current DUR: " + jpSpecMbo.getString("NUMVALUE")
            jpSpecMbo.setValue("NUMVALUE",dur,MboConstants.NOACCESSCHECK)
            print "Current UOM: " + jpSpecMbo.getString("MEASUREUNITID")
            jpSpecMbo.setValue("MEASUREUNITID",uom,MboConstants.NOACCESSCHECK)
        jpSpecMboSet.save()
else:
   print "##ERROR## Job Plan classification doesn't exist."