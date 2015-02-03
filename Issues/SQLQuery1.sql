declare  @MinDate date;
declare  @MaxDate date;
declare  @location varchar(20);
declare  @region varchar(20);

set  @location = '1000077';
set  @region = 'I25';
set  @MinDate = '2014-01-01 00:00:00.000';
set  @MaxDate = '2016-03-31 00:00:00.000';



select monthrange.fcWeek,monthrange.fcMonthName,monthrange.fcYear,   pm.pmnum,pm.description,
isnull(locations.description,assetlocdesc.description ) locdesc,pm.assetnum
,pmforecastjp.jpnum,
convert(varchar,interval*frequency) + ' ' + pm.frequnit freqtext from

 (SELECT  TOP (DATEDIFF(DAY, @MinDate, @MaxDate) + 1)
        fcWeek= DATEPART( wk,DATEADD(DAY, ROW_NUMBER() OVER(ORDER BY a.object_id) - 1, @MinDate)),
        fcMonth = DATEPART( mm,DATEADD(DAY, ROW_NUMBER() OVER(ORDER BY a.object_id) - 1, @MinDate)),
        fcYear = DATEPART( YEAR,DATEADD(DAY, ROW_NUMBER() OVER(ORDER BY a.object_id) - 1, @MinDate)),
        fcMonthName = DATENAME( month,DATEADD(DAY, ROW_NUMBER() OVER(ORDER BY a.object_id) - 1, @MinDate))
FROM    sys.all_objects a
        CROSS JOIN sys.all_objects b ) monthrange

left outer join pmforecast on monthrange.fcMonth = DATEPART( mm,pmforecast.forecastdate) and monthrange.fcWeek = DATEPART( wk,forecastdate)	 and monthrange.fcYear = DATEPART( YEAR,forecastdate)
left outer join pm on pm.pmnum = pmforecast.pmnum 
left outer join asset on pm.assetnum = asset.assetnum
left outer join locations assetlocdesc on asset.location = assetlocdesc.location 
left outer join pmforecastjp on pmforecast.pmnum = pmforecastjp.pmnum and pmforecast.forecastseqno=pmforecastjp.forecastseqno
left outer join pmsequence on pmforecastjp.pmnum = pmsequence.pmnum and pmforecastjp.jpnum = pmsequence.jpnum
left outer join locations on pm.location = locations.location 
left outer join locationspec lsbbc on pm.location = lsbbc.location and lsbbc.assetattrid = 'BBCREG'
left outer join locationspec lsirv on pm.location = lsirv.location and lsirv.assetattrid = 'IRVREG'
left outer join locationspec lsio on pm.location = lsio.location and lsio.assetattrid = 'I25/O25'
where (
exists (select 1 from dbo.locancestor where ancestor in  (@location) and location =pm.location) 
or exists (select assetnum from asset where assetnum = pm.assetnum and exists (select 1 from dbo.locancestor where ancestor in  (@location) and location =asset.location))
or lsbbc.alnvalue in (@region)
or lsirv.alnvalue in (@region)
or lsio.alnvalue in (@region)
)
group by monthrange.fcWeek,monthrange.fcMonthName,monthrange.fcYear,   pm.pmnum,pm.description,
isnull(locations.description,assetlocdesc.description ) ,pm.assetnum
,pmforecastjp.jpnum,
convert(varchar,interval*frequency) + ' ' + pm.frequnit 





select count(*) from locationspec