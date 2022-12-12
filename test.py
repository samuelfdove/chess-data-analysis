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
newtell = -1
for i in reversed(range(2324107)):
  if i==0:
    break
  if i==1:
    newtell = 0
  else:
    db.execute("update games set tell=(select tell from games where gameid="+str(i-1)+") where tell="+str(i))

  print(i)


db.commit()


