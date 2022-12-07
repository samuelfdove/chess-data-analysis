import chess
import sqlite3
import chess.pgn
import chess.engine
import stockfish
import chess.polyglot
import asyncio

b= chess.Board("rnbqkb1r/ppp1pppp/5n2/3p4/4P3/2N5/PPPP1PPP/R1BQKBNR w KQkq - 2 3")
b = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

moves = b.legal_moves
for move in moves:

  if move.uci()=='a2a3':
    print(move)

    if b.turn:
      print("White")
    else:
      print("Black")
    print(b.is_capture(move))
    print(chess.piece_name(b.piece_at(move.from_square).piece_type))
    if b.is_capture(move):
      print(chess.piece_name(b.piece_at(move.to_square).piece_type))
    else:
      print('not capture')
    print(b.is_check())
    b.push(move)
    print(b.ply())
    print(b.fen())
    print(chess.square_file(move.from_square))
    print(chess.square_rank(move.from_square))
    print(chess.square_file(move.to_square))
    print(chess.square_rank(move.to_square))
    print(chess.square_distance(move.from_square,move.to_square))
    print(type(chess.square_rank(move.to_square)))
    if move.promotion==None:
      print('')
    else:
      print(chess.piece_name(move.promotion))
    print(move.uci())
    print(b.is_check())
    break

print('------')
db = sqlite3.connect("gameheaders.db")
curr = db.cursor()
curr.execute("SELECT tell from games where tell not in (select tell from allmoves)")
rows = curr.fetchone()
print(rows[0])
rows = curr.fetchone()
print(rows)

rows = curr.fetchall()
print(rows[0][0])