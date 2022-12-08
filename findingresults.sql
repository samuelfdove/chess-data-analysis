select * from allmoves limit 100;

select piece,avg(distance) from allmoves group by piece;

select fromsquarerank,fromsquarefile,piece from allmoves group by fromsquarefile,fromsquarerank,piece

select piece,COUNT(moveid);

select MAX(WhiteElo),MAX(BlackElo) from games where WhiteElo<>'?' and BlackElo<>'?';
select round((WhiteElo+BlackElo)/400)*200,WhiteElo,BlackElo,games.* from games;