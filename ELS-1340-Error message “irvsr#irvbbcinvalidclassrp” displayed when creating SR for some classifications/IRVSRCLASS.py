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