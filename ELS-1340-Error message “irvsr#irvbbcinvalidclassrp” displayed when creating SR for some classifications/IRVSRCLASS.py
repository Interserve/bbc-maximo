from psdi.mbo import MboConstants
from psdi.server import MXServer
from psdi.mbo import SqlFormat

mxServer = MXServer.getMXServer()
userInfo = mbo.getUserInfo()

V_CLASSSTRUCTUREID =  mbo.getString("CLASSSTRUCTUREID")

# You should not be able to pick the top level Classification
classAncSet = mxServer.getMboSet("CLASSANCESTOR", userInfo)
classAncSet.setWhere("CLASSSTRUCTUREID='" +V_CLASSSTRUCTUREID+ "'")
classAncSet.reset()
classCount = classAncSet.count()
if classCount == 1 :
	errorgroup = "irvsr"
	errorkey="irvbbcinvalidclass"
else:
       mbo.setValue("CLASSSTRUCTUREID",V_CLASSSTRUCTUREID ,MboConstants.NOACCESSCHECK)
      
       RPmboSet = mxServer.getMboSet("PLUSPRESPPLAN", userInfo)       
       RPmboSet.setWhere("CLASSSTRUCTUREID='" +V_CLASSSTRUCTUREID+ "' and status = 'ACTIVE'")
       RPmboSet.reset()
       count = RPmboSet.count()
       if count != 0:
            RPmbo = RPmboSet.getMbo(0)
            cusPri = RPmbo.getString("IRVCUSTPRI")
	    sanum = RPmbo.getString("SANUM")
            mbo.setValue("IRVCUSTPRI",cusPri ,MboConstants.NOACCESSCHECK)
	    
       else:

             RPmboSet = mbo.getMboSet("IRV_RP")     
             RPmboSet.setOrderBy("ranking")
             RPmboSet.reset()
             RPmbo = RPmboSet.getMbo(0)
             try:
                   cusPri = RPmbo.getString("IRVCUSTPRI")
	           sanum = RPmbo.getString("SANUM")
                   mbo.setValue("IRVCUSTPRI",cusPri ,MboConstants.NOACCESSCHECK)
	          
             except :
           
	           errorgroup = "irvsr"
	           errorkey="irvbbcinvalidclassrp"