import chess
import sqlite3
import chess.pgn
import chess.engine
import stockfish
import chess.polyglot
import asyncio

db = sqlite3.connect("gameheaders.db")
pgns = open("lichess_db_standard_rated_2015-06.pgn",'r')

##creating tables
#db.execute("DROP TABLE moves")
#db.execute("CREATE TABLE moves (moveid INTEGER PRIMARY KEY AUTOINCREMENT, tell INTEGER, nummoves INT, move1 VARCHAR(5), move2 VARCHAR(5), move3 VARCHAR(5), move4 VARCHAR(5), offbookply INT)")

db.commit()

reader = chess.polyglot.open_reader("baron30.bin")
tell=str(pgns.tell())
game = chess.pgn.read_game(pgns)
j=1
while game != None:
  
  board = game.board()
  moves = ["''","''","''","''"]
  nummoves=str(game.end().ply())
  offbookply = 0

  isbook=1
  i=1
  for move in game.mainline_moves():
    

    if isbook==1: #last move was book
      isbook=0
      for entry in reader.find_all(board):
        if move==entry.move:
          isbook=1
    
    board.push(move)

    if isbook==0 and offbookply==0:
      offbookply = board.ply()+1

    if board.ply()<=4:
      moves[board.ply()-1]="'"+move.uci()+"'"

    if offbookply!=0 and board.ply()>4:
      break
  
  valuestring = ','.join([tell,nummoves,moves[0],moves[1],moves[2],moves[3],str(offbookply)])
  #print("INSERT INTO moves (tell,nummoves,move1,move2,move3,move4,offbookply) VALUES ("+valuestring+")")
  db.execute("INSERT INTO firstmoves (tell,nummoves,move1,move2,move3,move4,offbookply) VALUES ("+valuestring+")")
  if j%500==0:
    db.commit()
  if j%1000==0:
    print(j)
  j+=1
  tell=str(pgns.tell())
  game=chess.pgn.read_game(pgns)
db.commit()


  # CREATE TABLE "firstmoves" (
	# "moveid"	INTEGER,
	# "tell"	INTEGER,
	# "nummoves"	INTEGER,
	# "move1"	VARCHAR(5),
	# "move2"	VARCHAR(5),
	# "move3"	VARCHAR(5),
	# "move4"	VARCHAR(5),
	# "offbookply"	INTEGER,
	# PRIMARY KEY("moveid" AUTOINCREMENT),
	# FOREIGN KEY("tell") REFERENCES games("tell"));