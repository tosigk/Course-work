## Name: Giuliana Tosi
## TicTacToe.py
##
## Purpose: A Tic Tac Toe game
##
## Input: MouseClicks
## Output: graphics

from graphics import *

##setting window boundaries
width = 500
height = 500
win = GraphWin('Tic Tac Toe', width, height)

#adding lines
lines = []
#vertical lines
lines.append(Line(Point(width/3,0), Point(width/3,height)))
lines.append(Line(Point(width/(3/2),0), Point(width/(3/2), height)))
#Horizontal lines
lines.append(Line(Point(0,height/3), Point(width,height/3)))
lines.append(Line(Point(0,height/(3/2)), Point(width,height/(3/2))))
#Loop to draw lines
for i in lines:
    i.draw(win)

#adding space to put x and o
letter = []
#first horizontal row
letter.append(Text(Point(width/6,height/6), ' '))
letter.append(Text(Point(width/2,height/6), ' '))
letter.append(Text(Point(width/1.2,height/6), ' '))
#second horizontal row
letter.append(Text(Point(width/6,height/2), ' '))
letter.append(Text(Point(width/2,height/2), ' '))
letter.append(Text(Point(width/1.2,height/2), ' '))
#third horizontal row
letter.append(Text(Point(width/6,height/1.2), ' '))
letter.append(Text(Point(width/2,height/1.2), ' '))
letter.append(Text(Point(width/1.2,height/1.2), ' '))

#Dictionary to convert x and y column and row values from point clicked
boardConverter = {(1,1):0,(2,1):1,(3,1):2,(1,2):3,(2,2):4,(3,2):5,(1,3):6,(2,3):7,(3,3):8}

for i in letter:
    i.draw(win)

#Space where messages appear
message = Text(Point(width/2,height/1.03), ' ')
message.draw(win)

#Creating the board
def buildBoard():
    list = []
    for i in range(1, 10):
        list.append(i)
    return list

#determining when a move is valid or not
def isLegal(board, spot):
    valid = False
    if spot >= 0 and spot < 9:
        valid = True

    if board[spot] == "x" or board[spot] == "o":
        valid = False

    return valid

#This undraws the empty spot so an x or o can replace it
def fillSpot(board, spot, char):
    board[spot] = char
    letter[spot].undraw()
    letter[spot].setText(char)
    letter[spot].draw(win)

#determines the winning situations
def isGameWon(board):
    if board[0:3] == ['x', 'x', 'x'] or board[0:3] == ['o', 'o', 'o']:
        return True
    elif board[3:6] == ['x', 'x', 'x'] or board[3:6] == ['o', 'o', 'o']:
        return True
    elif board[6:] == ['x', 'x', 'x'] or board[6:] == ['o', 'o', 'o']:
        return True
    elif board[0:7:3] == ['x', 'x', 'x'] or board[0:7:3] == ['o', 'o', 'o']:
        return True
    elif board[1::3] == ['x', 'x', 'x'] or board[1::3] == ['o', 'o', 'o']:
        return True
    elif board[2::3] == ['x', 'x', 'x'] or board[2::3] == ['o', 'o', 'o']:
        return True
    elif board[2:7:2] == ['x', 'x', 'x'] or board[2:7:2] == ['o', 'o', 'o']:
        return True
    elif board[0::4] == ['x', 'x', 'x'] or board[0::4] == ['o', 'o', 'o']:
        return True
    else:
        return False

#Determines when the game is over either if someone won or if its a tie
def isGameOver(board, numPlays):
    if isGameWon(board) == True:
        return True
    elif numPlays >= 9:
        return True
    else:
        return False

def main():
    gameOver = False
    player = 'x'
    board = buildBoard()
    moves = 0
    #While loop that continues until the game is won or a tied
    while gameOver is False:
        #getting x and y
        click = win.getMouse()
        x = click.getX()
        y = click.getY()
        #determing the column/row number based on where the user clicked
        xcolumn = None
        yrow = None
        if x < width/3:
            xcolumn = 1
        elif x < width/(3/2) and x > width/3:
            xcolumn = 2
        elif x > width/(3/2):
            xcolumn = 3
        if y < height/3:
            yrow = 1
        elif y > height/3 and y < height/(3/2):
            yrow = 2
        elif y > height/(3/2):
            yrow = 3
        #converts x and y column/row to the list index
        spot = boardConverter[(xcolumn, yrow)]
        #if legal fill with an x or o value
        if isLegal(board, spot) == True:
            fillSpot(board, spot, player)
            moves += 1
            #making the message x or o wins based on who won
            if isGameWon(board):
                message.undraw()
                message.setText(player + ' ' + 'Wins!\nClick to Close')
                message.draw(win)
                break
            #making the message a tie if no one wins
            elif moves >= 9:
                message.setText("It's a Tie!\nClick to Close")
                break
            #switching between x and o
            else:
                if player == 'x':
                    player = 'o'
                elif player == 'o':
                    player = 'x'
        #creating message saying it's an invalid spot
        else:
            message.setText('Invalid Spot')



    win.getMouse()






main()