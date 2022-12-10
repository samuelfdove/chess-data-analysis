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

#PIECE FROM SQUARE COUNTS IGNORE BOOK
df = pd.read_sql_query("select fromsquarerank,fromsquarefile,piece,COUNT(*) from allmoves where isbook=0 group by fromsquarerank,fromsquarefile,piece",db)
df.to_csv('results/piece_from_square_counts_ignore_book.csv',index=False)

#PIECE TO SQUARE COUNTS IGNORE BOOK
df = pd.read_sql_query("select tosquarerank,tosquarefile,piece,COUNT(*) from allmoves where isbook=0 group by tosquarerank,tosquarefile,piece",db)
df.to_csv('results/piece_to_square_counts_ignore_book.csv',index=False)

