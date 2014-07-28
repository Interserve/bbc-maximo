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
       RPmbo = mbo.getMboSet("IRV_RP").getMbo(0)
       try:
            cusPri = RPmbo.getString("IRVCUSTPRI")
            mbo.setValue("IRVCUSTPRI",cusPri ,MboConstants.NOACCESSCHECK)

       except :
           errorgroup = "irvsr"
           errorkey="irvbbcinvalidclassrp"