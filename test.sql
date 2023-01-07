delete from gameExtraData;

select avgrating, case when numgames/1000 < 1 then 'Other' else Open end as 'Opening', sum(numgames) from (select avgrating,E.Opening as 'Open',COUNT(*) as 'numgames' from games join gameExtraData using (tell) join ECOtoOpening E using (ECO) group by E.Opening,avgrating) T group by avgrating, Opening;

select avgrating, case when numgames/1000 < 1 then 'Other' else Open end as 'Opening', sum(numgames) from (select avgrating,E.Opening as 'Open',COUNT(*) as 'numgames' from games join gameExtraData using (tell) join ECOtoOpening E using (ECO) group by E.Opening,avgrating) T group by Opening;

select avgrating,Open,numgames,sum(numgames) over(PARTITION BY avgrating),(sum(numgames) over(PARTITION BY avgrating))/numgames from (select avgrating,E.Opening as 'Open',COUNT(*) as 'numgames' from games join gameExtraData using (tell) join ECOtoOpening E using (ECO) group by avgrating,E.Opening) t order by 5 desc;

select avgrating,Opening,sum(numgames) as 'numgames' from (select avgrating,numgames,case when (sum(numgames) over(PARTITION BY avgrating))/numgames > 20 then 'Other' else Open end as 'Opening' from (select avgrating,E.Opening as 'Open',COUNT(*) as 'numgames' from games join gameExtraData using (tell) join ECOtoOpening E using (ECO) group by avgrating,E.Opening) t) t2 group by avgrating,Opening;

select avgrating,Opening,sum(numgames) as 'numgames' from (select avgrating,numgames,case when (sum(numgames) over(PARTITION BY avgrating))/numgames > 20 then 'Other' else Open end as 'Opening' from (select avgrating,E.Opening as 'Open',COUNT(*) as 'numgames' from games join gameExtraData using (tell) join ECOtoOpening E using (ECO) group by avgrating,E.Opening) t) t2 group by Opening;


select avgrating, SUM(numgames) from (select avgrating,E.Opening as 'Open',COUNT(*) as 'numgames' from games join gameExtraData using (tell) join ECOtoOpening E using (ECO) group by E.Opening,avgrating) T group by avgrating;
