import random
from urllib.request import urlopen
import urllib.request
import os

HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    😀  |
        |
        |
       ===''', '''
    +---+
    😀  |
     |  |
        |
       ===''', '''
    +---+
    😰  |
   / |  |
        |
       ===''', '''
    +---+
   😰   |
   /|\  |
        |
       ===''', '''
    +---+
   😱   |
   /|\  |
   /    |
       ===''', '''
    +---+
    💀  |
   /|\  |
   / \  |
       ===''']


TARGET_URL = 'https://raw.githubusercontent.com/Bmumpo/HMAN/main/words.txt'
DATA = urllib.request.urlopen(TARGET_URL)
words=[]
for line in DATA:
     words.append(str(line).replace('b\'',"").replace('\\r\\n\'',""))

class gameBoard:
    def __init__(self,word):
        self.wrong = 0
        self.word=word.lower()
        self.completed=False
        self.guesses= []
    def drawBoard(self):
        placeholders="\t"
        for letter in board.word:
            if letter.lower() in board.guesses:
                placeholders = "{} {}".format(placeholders,letter)
            else:
                placeholders = "{} {}".format(placeholders,"_")
        if "_" not in placeholders:
            board.completed = True
        print (HANGMAN_PICS[board.wrong],placeholders, "\nGuesses:",*board.guesses)
    

board=gameBoard(random.choice(words))
 
running = True

while running:
 board.drawBoard()
 guess=input ("Select a letter: ")[0]
 if guess not in board.guesses :
    board.guesses.append(guess.lower())
    if guess not in board.word:
        board.wrong +=1
 else:
    print ("Already Guessed") 
board.drawBoard() 

if (board.wrong == 6  ):
    input ("You lose: Press any key to restart")
if board.completed:
    input ("You won: Press any key to restart")
board=gameBoard(random.choice(words)) 
board.drawBoard()

 


 