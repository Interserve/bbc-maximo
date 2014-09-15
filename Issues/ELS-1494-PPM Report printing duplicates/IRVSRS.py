from java.lang import String
from java.lang import Integer
from psdi.mbo import MboConstants

# Add the gl account code components from the response plan and location gl codes

if mbo.isModified("status") and mbo.getString("STATUS") == "INPROG":
   mbo.setValueNull("ACTUALSTART", MboConstants.NOACCESSCHECK)
   


if mbo.isModified("status") and mbo.getString("STATUS") == "RESOLVED":
   mbo.setValueNull("ACTUALFINISH", MboConstants.NOACCESSCHECK)

   woSet = mbo.getMboSet("IRVWORKORDERAS")
   woSet.setWhere("actfinish is not null")
   woSet.reset()
   woSet.setOrderBy("actfinish desc")
   woSet.reset()
   woCount =  woSet.count()

   if woCount >0:
      mbo.setValue("ACTUALFINISH",woSet.getMbo(0).getDate("ACTFINISH"), MboConstants.NOACCESSCHECK)
	  
   woSet = mbo.getMboSet("IRVWORKORDERAS")
   woSet.setWhere("actstart is not null")
   woSet.reset()
   woSet.setOrderBy("actstart asc")
   woSet.reset()
   woCount =  woSet.count()

   if woCount >0:
      mbo.setValue("ACTUALSTART",woSet.getMbo(0).getDate("ACTSTART"), MboConstants.NOACCESSCHECK)


if onupdate:
    if (mbo.isModified("glaccount")) and (mbo.isModified("pluspresponseplan")) and mbo.getMboValue("glaccount").getPreviousValue().toString() != "" :
        glpart1 = mbo.getMboValue("glaccount").getPreviousValue().toString()
        glpart2 = mbo.getMboValue("glaccount").toString()
        print 'glpart1: ' + glpart1
        print 'glpart2: ' + glpart2  
        pos1 = glpart1.index('-',0)
        pos2 = glpart2.index('-',0)
        print 'pos1: ' + Integer(pos1).toString()
        print 'pos2: ' + Integer(pos2).toString()
        mbo.setValue("glaccount",glpart1[:pos1] + glpart2[pos2:])
    elif (mbo.isModified("glaccount")) and (mbo.isModified("location")) and mbo.getMboValue("glaccount").getPreviousValue().toString() != "" :
        glpart1 = mbo.getMboValue("glaccount").toString()
        glpart2 = mbo.getMboValue("glaccount").getPreviousValue().toString()
        print 'glpart1: ' + glpart1
        print 'glpart2: ' + glpart2  
        pos1 = glpart1.index('-',0)
        pos2 = glpart2.index('-',0)
        print 'pos1: ' + Integer(pos1).toString()
        print 'pos2: ' + Integer(pos2).toString()
        mbo.setValue("glaccount",glpart1[:pos1] + glpart2[pos2:])