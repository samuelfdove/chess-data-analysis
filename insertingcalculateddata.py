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
db.execute("insert into gameExtraData ('tell','avgrating','Event') select tell,round((WhiteElo+BlackElo)/400)*200, case when Event like '%Bull%tourn%' then 'Rated Bullet tournament' when Event like '%blitz%tourn%' then 'Rated Blitz tournament' when Event like '%Rapid%tourn%' then 'Rated Rapid tournament' when Event like '%Class%tourn%' then 'Rated Classical tournament' else Event end from games;")
db.commit()
db.close()

# CREATE TABLE "gameExtraData" (
# 	"extradataid"	INTEGER,
# 	"tell"	INTEGER,
# 	"avgrating"	INTEGER,
# 	PRIMARY KEY("extradataid" AUTOINCREMENT),
# 	FOREIGN KEY("tell") REFERENCES "games"("tell")
# );