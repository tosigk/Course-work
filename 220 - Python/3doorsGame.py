## Name: Giuliana Tosi
## button.py
##
## Purpose: A guessing game with buttons
##
## Input: mouse clicks
## Output: graphics window

#imports
from graphics import *
import random
from button import Button
from time import sleep

#making the window
width = 500
height = 300
win = GraphWin('Three Doors Game', width, height)

#setting initializers
wins = 0
losses = 0
status = None

#creating the buttons for the bonus
menuButtons = []
menuButtons.append(Button(Rectangle(Point(width/2.5-100, height/1.5-20), Point(width/2.5, height/1.5+20)), 'Play Again'))
menuButtons.append(Button(Rectangle(Point(width/1.25-100, height/1.5-20), Point(width/1.25, height/1.5+20)), 'Quit'))

#creating the text messages
labels = []
labels.append(Text(Point(width/2, height/4), 'I have a secret door'))
labels.append(Text(Point(width/2, height/1.2), 'Click to choose my door'))

#creating the original game
def playGame():
    global wins
    global losses
    buttons = []
    buttons.append(Button(Rectangle(Point(width / 3 - 80, height / 2 - 20), Point(width / 3 - 20, height / 2 + 20)), 'Door 1'))
    buttons.append(Button(Rectangle(Point(width / 2 - 30, height / 2 - 20), Point(width / 2 + 30, height / 2 + 20)), 'Door 2'))
    buttons.append(Button(Rectangle(Point(width / 1.3 - 40, height / 2 - 20), Point(width / 1.3 + 20, height / 2 + 20)), 'Door 3'))
    labels[0].setText('I have a secret door')
    labels[1].setText('Click to choose my door')

#drawing the buttons
    for button in buttons:
        button.undraw()
        button.colorButton('white')
        button.draw(win)
        button.setLabel(win, button.label.getText())

#drawing the labels
    for label in labels:
        label.undraw()
        label.draw(win)

    randomButton = random.choice(buttons)
    status = None

#while loop to determine if the user guessed correctly or not and change color of button and change message to win or lose
    while True:
        click = win.getMouse()
        if randomButton.isClick(click) is True:
            wins += 1
            randomButton.setLabel(win, 'win')
            labels[0].setText('You Win!')
            labels[1].setText('')
            for i in range(3):
                randomButton.colorButton('green')
                sleep(0.3)
                randomButton.colorButton('white')
                sleep(0.3)
            randomButton.colorButton('green')
            status = 'win'
        else:
            for button in buttons:
                if button.isClick(click):
                    losses += 1
                    button.colorButton('red')
                    button.setLabel(win, 'lose')
                    status = 'lose'
                    labels[0].setText('You Lose!')
                    labels[1].setText(randomButton.label.getText()+' is my secret door')
                    sleep(3*.6)

        if status != None:
            break
    for button in buttons:
        button.undraw()
    showMenu()

#The window for the bonus part
def showMenu():
   global wins
   global losses
   menuStatus = None
   labels[0].setText('Wins '+str(wins)+'\nLosses '+str(losses))
   for button in menuButtons:
       button.undraw()
       button.draw(win)
   while True:
       click = win.getMouse()
       if menuButtons[0].isClick(click):
           menuStatus = "New Game"
           break
       elif menuButtons[1].isClick(click):
           break
   if menuStatus == 'New Game':
       for button in menuButtons:
            button.undraw()
       playGame()


playGame()
