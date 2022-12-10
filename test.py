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

df = pd.read_sql_query("SELECT fromsquarerank,fromsquarefile,piece from allmoves limit 10",db)
print(df)
df.to_csv('results/test.csv',index=False)