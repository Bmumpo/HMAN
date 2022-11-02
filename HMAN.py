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
   😱  |
   /|\  |
   /    |
       ===''', '''
    +---+
   💀  │
   /|\  │
   / \  │
       ===''']


TARGET_URL = 'https://raw.githubusercontent.com/Bmumpo/HMAN/main/words.txt'
DATA = urllib.request.urlopen(TARGET_URL)
words=[]
for line in DATA:
     words.append(str(line).replace('b\'',"").replace('\\r\\n\'',""))
running = True     

class gameBoard:
    def __init__(self,word):
        self.wrong = 0
        self.word=word.lower()
        self.completed=False
        self.guesses= []
        self.placeholders="_"

    def drawBoard(self):
        self.placeholders="\t"
        for letter in board.word:
            if letter.lower() in board.guesses:
                self.placeholders = "{} {}".format(self.placeholders,letter)
            else:
                self.placeholders = "{} {}".format(self.placeholders,"_")
         
        print (HANGMAN_PICS[board.wrong],self.placeholders, "\nGuesses:",*board.guesses)
    

board=gameBoard(random.choice(words))
 


while running:
   
    board.drawBoard()
    if (board.wrong >= len(HANGMAN_PICS)-1  ):
        print (f'Word was {board.word}')
        input ("You lose: Press any key to restart")
        board=gameBoard(random.choice(words)) 
        continue
    if "_" not in board.placeholders:
        input ("You won: Press any key to restart")
        board=gameBoard(random.choice(words)) 
        continue
   
    guess=input ("Select a letter: ").lower()
    if not guess :
        continue
    if guess[0] not in board.guesses and guess.isalpha():
        board.guesses.append(guess[0])
        if guess not in board.word:
            board.wrong +=1
    else:
        print ("Already Guessed or not a letter") 
     


 


 
