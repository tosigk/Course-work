## Name: Giuliana Tosi
## vigenere.py
##
## Purpose: Implement the vigenere cipher and encode the message
##
## Input:message and keyword
## Output: encoded message
from graphics import *

##Function to encode message with the keyword
def code(message, keyword):
    message = message
    keyword = keyword*(int(len(message)/len(keyword)+1))
    keyword = keyword[:len(message)]
    answer = ''
    alphabet = list(range(26))
    for i in range(len(keyword)):
        letter = alphabet[ord(keyword[i])-65:] + alphabet[:ord(keyword[i])-65]
        answer += chr(letter[ord(message[i])-65] + 65)
    return answer


def vigenere():

##setting window boundaries
    width = 500
    height = 300
    win = GraphWin('Vigenere', width, height)

##List of objects
    objectsList = []

##This will give instructions to the user to exit the window
    instructions = Text(Point(width/2, height/1.02), 'Click anywhere to close')
    instructions.setFace('courier')

##Creating the Messages for user to input code
    messageTextPt = Point(width/4, height/6)
    messageText = Text(messageTextPt, 'Message to code:')

    keywordTextPt = messageTextPt.clone()
    keywordTextPt.move(0,30)
    keywordText = Text(keywordTextPt, 'Enter keyword:')

##Entry boxes
    messageInput = Entry(Point(width/2, height/6), 12)
    messageInput.draw(win)

    keywordInput = Entry(Point(width/2, height/6+30), 12)
    keywordInput.draw(win)

##Encode textbox
    encodeRect = Rectangle(Point(width*(1/3),height/3), Point(width*(2/3),height/2.2))
    encode = Text(Point(width/2,height/2.5), 'Encode')
    encode.setFace('courier')
    encode.setSize(20)

##Outputting the answer
    resultingMessage = Text(Point(width/2, height/1.7), 'Resulting Message')
    answer = Text(Point(width/2, height/1.5), '')

##Drawing graphics objects
    messageText.draw(win)
    keywordText.draw(win)
    encodeRect.draw(win)
    encode.draw(win)
    win.getMouse()

##Using my inputs to calcualte the encoded message
    messageI = messageInput.getText().upper().replace(' ', '')
    keywordI = keywordInput.getText().upper()


    encodedMessage = code(messageI, keywordI)
    resultingMessage.draw(win)
    answer.setText(encodedMessage)
    answer.draw(win)
    instructions.draw(win)
    win.getMouse()

    win.close()
vigenere()

