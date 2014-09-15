update workorder set glaccount = (select replace(glaccount,'-??????','')  from locations where locations.location = workorder.location) + '-'+ replace(glaccount,'??????????-','')  where glaccount like  '??????????-%' and worktype <> 'PPM' ;


update workorder set glaccount = (select replace(glaccount,'-??????','')  from locations where locations.location = workorder.location) + '-MEPMXF'  where  worktype= 'PPM' and  glaccount like  '%-???%' ;