## Name: Giuliana Tosi
## fallGreeting.py
##
## Purpose: Using graphics to creat a Thanksgiving greeting card.
##
## Input: Inputs: Click(mouse)
## Output: Outputs: Graphics image

##imports
from graphics import *
from time import sleep

##setting window boundaries
width = 500
height = 500
win = GraphWin('Happy Thanksgiving', width, height)

##This will give instructions to the user to exit the window
instructions = Text(Point(width/2, height/1.02), 'Click anywhere to close')
instructions.setFace('courier')

##Text file saying Happy Thanksgiving
message = Text(Point(width/2,height/8) , 'Happy Thanksgiving!')
message.setFace('courier')
message.setSize(30)

##Underlining Happy Thanksgiving
line = Line(Point(20,height/6.5), Point(460,height/6.5))

##Importing the pumpkin image
pumpkin = Image(Point(width/2, height/1.8), 'pumpkin2.gif')

##Creating eyes, a mouth, and a nose for the pumpkin
eye1 = Circle(Point(150,275), 20)
eye1.setOutline('gold')
eye1.setFill('gold')
eye2 = eye1.clone()
eye2.move(200, 0)

mouth = Oval(Point(150,375), Point(340,425))
mouth.setFill('gold')
mouth.setOutline('gold')

nose = Polygon(Point(205,338), Point(280,338), Point(242,285))
nose.setFill('gold')
nose.setOutline('gold')

##Setting the background a different color
win.setBackground('firebrick')

##drawing the functions in main
def main():

    message.draw(win)
    line.draw(win)
    pumpkin.draw(win)
    eye1.draw(win)
    eye2.draw(win)
    mouth.draw(win)
    nose.draw(win)

##A for loop to have the eyes, mouth, nose, and underline flash different colors
    for i in range(15):
        line.setFill('orange')
        eye1.setFill('orange')
        eye2.setFill('orange')
        mouth.setFill('orange')
        nose.setFill('orange')
        sleep(.3)
        eye1.setFill('gold')
        eye2.setFill('gold')
        mouth.setFill('gold')
        nose.setFill('gold')
        line.setFill('black')
        sleep(.3)

    instructions.draw(win)
    win.getMouse()
    win.close()
main()