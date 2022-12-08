select tell,round((WhiteElo+BlackElo)/400)*200 from games;

insert into gameExtraData ("tell","avgrating") select tell,round((WhiteElo+BlackElo)/400)*200 from games;
insert into gameExtraData ("extradataid","tell","avgrating") values (NULL,671,1400);

select * from gameExtraData;