import chess
import sqlite3
import chess.pgn
import chess.engine
import chess.polyglot
import stockfish

db = sqlite3.connect("gameheaders2.db")
pgns = open("lichess_db_standard_rated_2015-06.pgn",'r')

##creating tables
# db.execute("DROP TABLE games")
# db.execute("CREATE TABLE games (gameid INTEGER PRIMARY KEY, tell INTEGER, Site char(50), White char(30), Black char(30), WhiteElo int, BlackElo int, Result char(10), ECO char(10), Opening char(50), Termination char(30), TimeControl char(30), UTCDate char(10), UTCTime char(8), Event char(100), WhiteRatingDiff char(10), BlackRatingDiff char(10), BlackTitle char(10), WhiteTitle char(10), Date char(50), Round char(10))")

db.commit()
tell = pgns.tell()
gameheaders = chess.pgn.read_headers(pgns)
j=1
while gameheaders != None:
  headers = list(gameheaders._tag_roster.keys())+list(gameheaders._others.keys())
  headersString=','.join(headers)

  valuesString = '"'+str(tell)+'"'
  for i in range(0,len(headers)):
    valuesString+=',"'+gameheaders[headers[i]]+'"'


  try:
    db.execute("INSERT INTO games (gameid, tell, "+headersString+") VALUES ("+str(j)+","+valuesString+")")
  except Exception as e:
    print("INSERT INTO games (gameid, tell,"+headersString+") VALUES ("+str(j)+","+valuesString+")")
    print(e)
    input()

  
  
  if j%100000==0:
    db.commit()
    print(j)
  j+=1
  tell = pgns.tell()
  gameheaders=chess.pgn.read_headers(pgns)

db.commit()
print('done')