import chess
import sqlite3
import chess.pgn
import chess.engine
import stockfish
import chess.polyglot
import asyncio
import matplotlib as plt
import pandas as pd
import numpy as np
import seaborn as sns 
import csv

db = sqlite3.connect("gameheaders.db")

# #PIECE FROM SQUARE COUNTS
# df = pd.read_sql_query("select fromsquarerank,fromsquarefile,piece,COUNT(*) from allmoves group by fromsquarerank,fromsquarefile,piece",db)
# df.to_csv('results/piece_from_square_counts.csv',index=False)

# #PIECE TO SQUARE COUNTS
# df = pd.read_sql_query("select tosquarerank,tosquarefile,piece,COUNT(*) from allmoves group by tosquarerank,tosquarefile,piece",db)
# df.to_csv('results/piece_to_square_counts.csv',index=False)

# #PIECE FROM SQUARE COUNTS IGNORE FIRST 10
# df = pd.read_sql_query("select fromsquarerank,fromsquarefile,piece,COUNT(*) from allmoves where isbook=0 and ply > 10 group by fromsquarerank,fromsquarefile,piece",db)
# df.to_csv('results/piece_from_square_counts_ignore_10.csv',index=False)

# #PIECE TO SQUARE COUNTS IGNORE FIRST 10
# df = pd.read_sql_query("select tosquarerank,tosquarefile,piece,COUNT(*) from allmoves where isbook=0 and ply > 10 group by tosquarerank,tosquarefile,piece",db)
# df.to_csv('results/piece_to_square_counts_ignore_10.csv',index=False)

# #PIECE FROM SQUARE COUNTS BY SIDE
# df = pd.read_sql_query("select fromsquarerank,fromsquarefile,piece,COUNT(*),turn from allmoves where isbook=0 group by fromsquarerank,fromsquarefile,piece,turn",db)
# df.to_csv('results/piece_from_square_counts_by_side.csv',index=False)

# #PIECE TO SQUARE COUNTS BY SIDE
# df = pd.read_sql_query("select tosquarerank,tosquarefile,piece,COUNT(*),turn from allmoves where isbook=0 group by tosquarerank,tosquarefile,piece,turn",db)
# df.to_csv('results/piece_to_square_counts_by_side.csv',index=False)

# #PIECE TO SQUARE COUNTS BY SIDE BY SKILL
# df = pd.read_sql_query("select tosquarerank,tosquarefile,piece,COUNT(*),turn,case when avgrating<=1200 then 'Bad' when avgrating>=1800 then 'Good' else '-' end as 'Skill' from allmoves join gameExtraData using (tell) where avgrating<=1200 or avgrating>=1800 and isbook=0 group by tosquarerank,tosquarefile,piece,turn,Skill",db)
# df.to_csv('results/piece_to_square_counts_by_side_by_skill.csv',index=False)

# #PIECE TO SQUARE COUNTS BY SIDE BY ELO
# df = pd.read_sql_query("select tosquarerank,tosquarefile,piece,COUNT(*),turn,avgrating from allmoves join gameExtraData using (tell) group by tosquarerank,tosquarefile,piece,turn,avgrating",db)
# df.to_csv('results/piece_to_square_counts_by_side_by_rating.csv',index=False)

# #PIECE DISTANCE BY ELO --Didn't give much
# df = pd.read_sql_query("SELECT piece, avgrating, avg(distance) from allmoves join gameExtraData using (tell) group by piece, avgrating", db)
# df.to_csv('results/piece_distance_by_rating.csv', index=False)

# ##
# #PIECE FROM SQUARE COUNTS BY SIDE AND ELO
# df = pd.read_sql_query("select fromsquarerank,fromsquarefile,piece,COUNT(*),turn,avgrating from allmoves join gameExtraData using (tell) group by fromsquarerank,fromsquarefile,piece,turn,avgrating",db)
# df.to_csv('results/piece_from_square_counts_by_side_by_rating.csv',index=False)

# #PIECE TO SQUARE COUNTS BY SIDE AND ELO
# df = pd.read_sql_query("select tosquarerank,tosquarefile,piece,COUNT(*),turn,avgrating from allmoves join gameExtraData using (tell) group by tosquarerank,tosquarefile,piece,turn,avgrating",db)
# df.to_csv('results/piece_to_square_counts_by_side_by_rating.csv',index=False)

# df = pd.read_sql_query("select tosquarerank+1 as 'tosquarerank',tosquarefile+1 as 'tosquarefile',piece,COUNT(*),turn,avgrating from allmoves join gameExtraData using (tell) group by tosquarerank,tosquarefile,piece,turn,avgrating order by tosquarerank desc,tosquarefile asc",db)
# df.to_csv('results/piece_to_square_counts_by_side_by_rating_p1.csv',index=False)

# df = pd.read_sql_query("select tosquarerank+1 as 'tosquarerank',tosquarefile+1 as 'tosquarefile',piece,COUNT(*),turn,avgrating from allmoves join gameExtraData using (tell) where isbook = 0 and ply>20 group by tosquarerank,tosquarefile,piece,turn,avgrating order by tosquarerank desc,tosquarefile asc",db)
# df.to_csv('results/piece_to_square_counts_by_side_by_rating_p1_no_book.csv',index=False)

# #PIECE TO PIECE CAPTURE DATA
# df = pd.read_sql_query("select piece,capturedpiece,COUNT(*) from allmoves where iscapture='True' group by piece,capturedpiece", db)
# df.to_csv('results/piece_to_piece_capture_data.csv',index=False)

# #PIECE TO PIECE CAPTURE DATA BY ELO
# df = pd.read_sql_query("select piece,capturedpiece,COUNT(*),avgrating from allmoves join gameExtraData using(tell) where iscapture='True' group by piece,capturedpiece,avgrating", db )
# df.to_csv('results/piece_to_piece_capture_data_by_rating.csv',index=False)

# #PIECE TO PIECE CAPTURE DATA BY SKILL
# df = pd.read_sql_query("select piece,capturedpiece,COUNT(*),case when avgrating<=1200 then 'Bad' when avgrating>=1800 then 'Good' else '-' end as 'Skill' from allmoves join gameExtraData using(tell) where (avgrating<=1200 or avgrating>=1800) and iscapture='True' group by piece,capturedpiece,Skill", db )
# df.to_csv('results/piece_to_piece_capture_data_by_skill.csv',index=False)

# #PIECE CAUSE CHECK
# df = pd.read_sql_query("select piece,COUNT(*) from allmoves where ischeck='True' group by piece", db)
# df.to_csv('results/piece_cause_check.csv',index=False)

# #PIECE CAUSE CHECK BY ELO
# df = pd.read_sql_query("select piece,COUNT(*),avgrating from allmoves join gameExtraData using (tell) where ischeck='True' group by piece,avgrating", db)
# df.to_csv('results/piece_cause_check_by_rating.csv',index=False)

# #PIECE CAUSE CHECK BY SKILL
# df = pd.read_sql_query("select piece,COUNT(*),case when avgrating<=1200 then 'Bad' when avgrating>=1800 then 'Good' else '-' end as 'Skill' from allmoves join gameExtraData using (tell) where (avgrating<=1200 or avgrating>=1800) and ischeck='True' group by piece,skill", db)
# df.to_csv('results/piece_cause_check_by_rating.csv',index=False)

# #PIECE AFTER CHECK
# df = pd.read_sql_query("select piece,COUNT(*) from allmoves where isincheck='True' group by piece", db)
# df.to_csv('results/piece_after_check.csv',index=False)

# #PIECE AFTER CHECK BY ELO
# df = pd.read_sql_query("select piece,COUNT(*),avgrating from allmoves join gameExtraData using (tell) where isincheck='True' group by piece,avgrating", db)
# df.to_csv('results/piece_after_check_by_rating.csv',index=False)

# #PIECE AFTER CHECK BY SKILL
# df = pd.read_sql_query("select piece,COUNT(*),case when avgrating<=1200 then 'Bad' when avgrating>=1800 then 'Good' else '-' end as 'Skill' from allmoves join gameExtraData using (tell) where (avgrating<=1200 or avgrating>=1800) and isincheck='True' group by piece,skill", db)
# df.to_csv('results/piece_after_check_by_rating.csv',index=False)

# df = pd.read_sql_query("select avgrating,COUNT(*) from allmoves join gameExtraData using (tell) group by avgrating", db)
# df.to_csv('results/rating_move_amounts.csv',index=False)

# df = pd.read_sql_query("select avgrating,piece,COUNT(*) as 'nummoves' from allmoves join gameExtraData using (tell) group by piece,avgrating", db)
# df.to_csv('results/piece_move_amounts_by_rating.csv',index=False)

# df = pd.read_sql_query("select avgrating,Termination,COUNT(*) as 'numgames' from games join gameExtraData using (tell) group by Termination,avgrating", db)
# df.to_csv('results/termination_by_rating.csv',index=False)

# df = pd.read_sql_query("select avgrating,E.Opening,COUNT(*) as 'numgames' from games join gameExtraData using (tell) join ECOtoOpening E using (ECO) group by E.Opening,avgrating", db)
# df.to_csv('results/opening_by_rating.csv',index=False)

# df = pd.read_sql_query("select avgrating,move1,move2,move3,move4,COUNT(*) as 'numgames' from firstmoves join gameExtraData using (tell) group by avgrating,move1,move2,move3,move4", db)
# df.to_csv('results/firstmoves_by_rating.csv',index=False)

# df = pd.read_sql_query("select avgrating,move1,move2,COUNT(*) as 'numgames_firstmoves' from firstmoves join gameExtraData using (tell) group by avgrating,move1,move2", db)
# df.to_csv('results/firstmoves_by_rating_2.csv',index=False)

# df = pd.read_sql_query("select avgrating,nummoves,COUNT(*) as 'numgames' from firstmoves join gameExtraData using (tell) group by avgrating,nummoves", db)
# df.to_csv('results/nummoves_by_rating.csv',index=False)

# df = pd.read_sql_query("select avgrating,ged.Event,COUNT(*) as 'numgames' from games join gameExtraData ged using (tell) group by avgrating,ged.Event", db)
# df.to_csv('results/Event_by_rating.csv',index=False)

# df = pd.read_sql_query("select avgrating,Opening,sum(numgames) as 'numgames' from (select avgrating,numgames,case when (sum(numgames) over(PARTITION BY avgrating))/numgames > 50 then 'Other' else Open end as 'Opening' from (select avgrating,E.Opening as 'Open',COUNT(*) as 'numgames' from games join gameExtraData using (tell) join ECOtoOpening E using (ECO) group by avgrating,E.Opening) t) t2 group by avgrating,Opening;", db)
# df.to_csv('results/Opening_by_rating_with_other.csv',index=False)

# df = pd.read_sql_query("select avgrating,piece,capturedpiece,COUNT(moveid) as 'nummoves_captures' from allmoves join gameExtraData ged using (tell) where iscapture='True' group by avgrating,piece,capturedpiece;", db)
# df.to_csv('results/Captures_by_rating.csv',index=False)

# df = pd.read_sql_query("select avgrating, piece, COUNT(*) as 'numcheckmates' from allmoves join firstmoves using (tell) join gameExtraData using (tell) join games using (tell) where ischeck='True' and Termination='Normal' and ply=nummoves group by avgrating, piece", db)
# df.to_csv('results/Checkmates_by_piece_by_rating.csv',index=False)

# df = pd.read_sql_query("select ROUND(ply/10)*10, piece, COUNT(*) as 'numcheckmates' from allmoves join firstmoves using (tell) join gameExtraData using (tell) join games using (tell) where ischeck='True' and Termination='Normal' and ply=nummoves group by ROUND(ply/10)*10, piece", db)
# df.to_csv('results/Checkmates_by_piece_by_ply.csv',index=False)

# df = pd.read_sql_query("select case when avgrating<=1200 then 'Bad' when avgrating>=1800 then 'Good' else '-' end as 'Skill', piece, COUNT(*) as 'numcheckmates' from allmoves join firstmoves using (tell) join gameExtraData using (tell) join games using (tell) where (avgrating<=1200 or avgrating>=1800) and ischeck='True' and Termination='Normal' and ply=nummoves group by Skill, piece", db)
# df.to_csv('results/Checkmates_by_piece_by_skill.csv',index=False)

# df = pd.read_sql_query("select case when avgrating<=1200 then 'Bad' when avgrating>=1800 then 'Good' else '-' end as 'Skill',piece,distance,COUNT(*) as 'number of moves' from allmoves join gameExtraData using (tell) where avgrating<=1200 or avgrating>=1800 group by 'Skill', piece,distance", db)
# df.to_csv('results/distance_by_piece_by_skill.csv',index=False)

# df = pd.read_sql_query("select ROUND(ply/10)*10, COUNT(*) as 'nummates',case when avgrating<=1200 then 'Bad' when avgrating>=1800 then 'Good' else '-' end as 'Skill' from allmoves join firstmoves using (tell) join gameExtraData using (tell) join games using (tell) where (avgrating<=1200 or avgrating>=1800) and ischeck='True' and Termination='Normal' and ply=nummoves group by ROUND(ply/10)*10, Skill", db)
# df.to_csv('results/checkmates_by_ply_by_skill.csv',index=False)

# df = pd.read_sql_query("select ROUND(ply/10)*10,piece, COUNT(*) as 'nummates',case when avgrating<=1200 then 'Bad' when avgrating>=1800 then 'Good' else '-' end as 'Skill' from allmoves join firstmoves using (tell) join gameExtraData using (tell) join games using (tell) where (avgrating<=1200 or avgrating>=1800) and ischeck='True' and Termination='Normal' and ply=nummoves group by ROUND(ply/10)*10,piece, Skill", db)
# df.to_csv('results/checkmates_by_piece_by_ply_by_skill.csv',index=False)

# df = pd.read_sql_query("select ROUND(ply/10)*10 as 'MoveNumber', COUNT(*) as 'numcaptures',case when avgrating<=1200 then 'Bad' when avgrating>=1800 then 'Good' else '-' end as 'Skill' from allmoves join gameExtraData using (tell) where (avgrating<=1200 or avgrating>=1800) and iscapture='True' group by ROUND(ply/10)*10, Skill", db)
# df.to_csv('results/captures_by_ply_by_skill.csv',index=False)

# df = pd.read_sql_query("select ROUND(ply/10)*10 as 'MoveNumber' ,capturedpiece, COUNT(*) as 'numcaptures',case when avgrating<=1200 then 'Bad' when avgrating>=1800 then 'Good' else '-' end as 'Skill' from allmoves join gameExtraData using (tell) where (avgrating<=1200 or avgrating>=1800) and iscapture='True' group by ROUND(ply/10)*10,capturedpiece, Skill", db)
# df.to_csv('results/captures_by_capturedpiece_by_ply_by_skill.csv',index=False)

# df = pd.read_sql_query("select ROUND(ply/10)*10 as 'MoveNumber',piece, COUNT(*) as 'nummoves',case when avgrating<=1200 then 'Bad' when avgrating>=1800 then 'Good' else '-' end as 'Skill' from allmoves  join gameExtraData using (tell) where (avgrating<=1200 or avgrating>=1800) group by ROUND(ply/10)*10,piece, Skill", db)
# df.to_csv('results/moves_by_piece_by_ply_by_skill.csv',index=False)

db.close()

