import alphaBetaPruning
import game

board=game.create()
game.whoIsFirst(board)
while not game.isFinished(board):
    if game.isHumTurn(board):
        game.inputMove(board)
    else:
        board=alphaBetaPruning.go(board)
game.printState(board)

