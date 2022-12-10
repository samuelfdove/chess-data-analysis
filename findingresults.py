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

# #PIECE TO SQUARE COUNTS IGNORE SIDE
# df = pd.read_sql_query("select tosquarerank,tosquarefile,piece,COUNT(*),turn from allmoves where isbook=0 group by tosquarerank,tosquarefile,piece,turn",db)
# df.to_csv('results/piece_to_square_counts_by_side.csv',index=False)

# #PIECE DISTANCE BY ELO --Didn't give much
# df = pd.read_sql_query("SELECT piece, avgrating, avg(distance) from allmoves join gameExtraData using (tell) group by piece, avgrating", db)
# df.to_csv('results/piece_distance_by_rating.csv', index=False)