import chess
import sqlite3
import chess.pgn
import chess.engine
import stockfish
import chess.polyglot
import asyncio


db = sqlite3.connect("gameheaders.db")
pgns = open("lichess_db_standard_rated_2015-06.pgn",'r')


db.commit()

reader = chess.polyglot.open_reader("baron30.bin")

game = chess.pgn.read_game(pgns)

curr = db.cursor()
curr.execute("SELECT tell from games where tell not in (select tell from allmoves)")
rows = curr.fetchall()
curr.close()
j=1
for i in range(len(rows)):
  
  b = game.board()
  tell=rows[i][0]
  pgns.seek(tell)
  game = chess.pgn.read_game(pgns)

  isbook=1
  for move in game.mainline_moves():

    if isbook==1: #last move was book
      isbook=0
      for entry in reader.find_all(b):
        if move==entry.move:
          isbook=1
    
    moveuci = move.uci()
    if b.turn:
      turn = "White"
    else:
      turn = "Black"
    piece = chess.piece_name(b.piece_at(move.from_square).piece_type)
    iscapture = b.is_capture(move)
    capturedpiece = 'None'
    if iscapture:
      if b.is_en_passant(move):
        capturedpiece='pawn'
      else:
        capturedpiece = chess.piece_name(b.piece_at(move.to_square).piece_type)
    promotionpiece = 'None'
    if move.promotion!=None:
      promotionpiece = chess.piece_name(move.promotion)
    isincheck = b.is_check()
    FENbefore = b.fen()
    b.push(move)
    ischeck = b.is_check()
    fromsquarefile = chess.square_file(move.from_square)
    fromsquarerank = chess.square_rank(move.from_square)
    tosquarefile = chess.square_file(move.to_square)
    tosquarerank = chess.square_rank(move.to_square)
    distance = chess.square_distance(move.from_square,move.to_square)
    ply = b.ply()


  
    valuestring = "'"+"','".join([str(tell),moveuci,str(ply),turn,str(isbook),piece,str(iscapture),capturedpiece,promotionpiece,str(isincheck),str(ischeck),str(fromsquarefile),str(fromsquarerank),str(tosquarefile),str(tosquarerank),str(distance),str(FENbefore)])+"'"
    #print("INSERT INTO allmoves (tell,move,ply,turn,isbook,piece,iscapture,capturedpiece,promotionpiece,isincheck,ischeck,fromsquarefile,fromsquarerank,tosquarefile,tosquarerank,distance,FENbefore) VALUES ("+valuestring+")")
    db.execute("INSERT INTO allmoves (tell,move,ply,turn,isbook,piece,iscapture,capturedpiece,promotionpiece,isincheck,ischeck,fromsquarefile,fromsquarerank,tosquarefile,tosquarerank,distance,FENbefore) VALUES ("+valuestring+")")
  if i%500==0:
    db.commit()
  if i%1000==0:
    print(i)
db.commit()


# CREATE TABLE "allmoves" (
# 	"moveid"	INTEGER,
# 	"tell"	INTEGER,
# 	"move"	TEXT,
# 	"ply"	INTEGER,
# 	"turn"	TEXT,
# 	"isbook"	TEXT,
# 	"piece"	TEXT,
# 	"iscapture"	TEXT,
# 	"capturedpiece"	TEXT,
# 	"promotionpiece"	TEXT,
# 	"isincheck"	TEXT,
# 	"ischeck"	TEXT,
# 	"fromsquarefile"	INTEGER,
# 	"fromsquarerank"	INTEGER,
# 	"tosquarefile"	INTEGER,
# 	"tosquarerank"	INTEGER,
# 	"distance"	INTEGER,
# 	"FENbefore"	TEXT,
# 	FOREIGN KEY("tell") REFERENCES "games"("tell"),
# 	PRIMARY KEY("moveid" AUTOINCREMENT)
# );