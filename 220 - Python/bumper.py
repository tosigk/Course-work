## Name: Giuliana Tosi
## bumper.py
##
## Purpose: A simulation of bumper cars
##
## Input: mouse clicks
## Output: graphics window

#imports
from random import randint
from graphics import *
import math
from time import sleep

#create window
width = 500
height = 500
win = GraphWin('Bumper Cars', width, height, autoflush=False)

instructions = Text(Point(width/2, height/1.02), 'Click anywhere to close')
instructions.setFace('courier')
instructions.draw(win)

#Calculate the distance between two points
def distance(Point1, Point2):
    distance = math.sqrt((Point1.getX()-Point2.getX())**2+(Point1.getY()-Point2.getY())**2)
    return distance

#Create a random color generator
def randomColor():
    color = color_rgb(randint(0,255),randint(0,255), randint(0,255))
    return color

#Make the cars in a list to be able to update them in main
cars = []

#Creates the circles(cars) in the window
class car():
    def __init__(self, point, angle, speed, radius, color):
        self.sprite = Circle(point, radius)
        self.sprite.setFill(color)
        self.sprite.draw(win)
        self.angle = angle
        self.speed = speed
        self.radius = radius
        cars.append(self)

#Create a function to move the car in different ways
    def move(self):
        y = (-1) * math.sin(self.angle) * (self.speed)
        x = math.cos(self.angle) * (self.speed)
        currentX = self.sprite.getCenter().getX()
        currentY = self.sprite.getCenter().getY()
        futureX = x + currentX
        futureY = y + currentY
        #controls angles/bouncing off of walls
        if futureX >= width - self.radius:
            self.angle += math.pi + 0.8
        elif futureX <= 0 + self.radius:
            self.angle += math.pi + 0.8
        elif futureY >= height - self.radius:
            self.angle += math.pi + 0.8
        elif futureY <= 0 + self.radius:
            self.angle += math.pi + 0.8
        #for loop to have cars bounce off each other
        for c in cars:
            if c != self:
                dist = distance(self.sprite.getCenter(), c.sprite.getCenter())
                if dist <= self.radius + c.radius:
                    self.angle += math.pi + 0.8
                    c.angle += math.pi + 0.8
                    self.sprite.setFill(randomColor())
                    c.sprite.setFill(randomColor())

        #Updates x and y calculations based off potentially new angle and moves car
        y = (-1) * math.sin(self.angle) * (self.speed)
        x = math.cos(self.angle) * (self.speed)
        self.sprite.move(x, y)



#Creates two car objects
car(Point(randint(30,width-30), randint(30,height-30)), randint(0, int(2*math.pi)), 5, 30, randomColor())
car(Point(randint(30,width-30), randint(30,height-30)), randint(0,int(2*math.pi)), 5, 30, randomColor())

#main function
def main():
    #infinte loop that breaks function that runs until the user clicks
    while True:
        for c in cars:
            c.move()
        click = win.checkMouse()
        if click != None:
            break
        win.update()
        sleep(1/100)

main()