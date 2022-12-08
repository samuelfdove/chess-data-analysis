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

db = sqlite3.connect("gameheaders.db")
db.execute('insert into gameExtraData ("tell","avgrating") select tell,round((WhiteElo+BlackElo)/400)*200 from games;')
db.commit()
db.close()

# CREATE TABLE "gameExtraData" (
# 	"extradataid"	INTEGER,
# 	"tell"	INTEGER,
# 	"avgrating"	INTEGER,
# 	PRIMARY KEY("extradataid" AUTOINCREMENT),
# 	FOREIGN KEY("tell") REFERENCES "games"("tell")
# );