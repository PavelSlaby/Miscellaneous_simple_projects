# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 12:55:36 2022

@author: pavel

# the hangman
"""

import numpy as np
from numpy import random
import re

words = ['apple', 'pear', 'house',  'mississippi']

l = len(words)
n = np.random.randint(0, l + 1)
word = words[n]

init_lives = 10
lives = init_lives
attempts = init_lives

spacing = 20
row_count = 21

text1 =  " " * 6 + "  ___________________________"
text2 =  " " * 6 + "||___________________________||"
text3 =  " " * 6 + "||" + " " * 27 + "||" 
text4 =  " " * 6 + "||" + " " * 27 + "||" 
text5 =  "    _____      " + " " * spacing + "||"
text6 =  "   /      \\    " + " " * spacing + "||"
text7 =  "  /  o  o  \\   " + " " * spacing + "||"
text8 =  "O|    I     |O " + " " * spacing + "||"
text9 =  " \   ___   /   " + " " * spacing + "||"
text10 = "  \       /    " + " " * spacing + "||"
text11 = "   \_____/     " + " " * spacing + "||"
text12 = "   __||__      " + " " * spacing + "||"
text13 = "  /      \     " + " " * spacing + "||"
text14 = " /  |  |  \    " + " " * spacing + "||"
text15 = "|   |  |   |   " + " " * spacing + "||"
text16 = "    \  /       " + " " * spacing + "||"
text17 = "     \/        " + " " * spacing + "||"
text18 = "     /\        " + " " * spacing + "||"
text19 = "    /  \       " + " " * spacing + "||"
text20 = "   /    \      " + " " * spacing + "||"
text21 = "  |      |     " + " " * spacing + "||"

text_list = ["text" + str(i) for i in range(1, 22)]


print("-" * 100)
print(" " * 45 + "Game of Hangman")
print("-" * 100)
instructions = """
Your task is to guess a word, by guessing single letters one at a time, you have {} lives. 
If you guess the letter incorectly, you lose one life.
You have {} attempts.
"""
print(instructions.format(init_lives, attempts))

guess = ["-" for i in range(0, len(word))]
n_attempt = 0

for i in range(0, attempts):
    
    guess_letter = input("make a guess:")
    
    if len(guess_letter) != 1 or not str(guess_letter).isalpha():
        print("you can insert only one letter")
           
    if guess_letter in word:
        indices = [i.start() for i in re.finditer(guess_letter, word)]
        for i in indices:
            guess[i] = guess_letter
            
        print("Good job, you guessed the letter correctly")
        
    else:
        lives -= 1 
        print("ooops that was wrong, you have {} lives remainings".format(lives) )        
   
    if guess.count("-") == 0 :
        print("congratulations, you have guessed it right. The word was {}. You made only {} guesses wrong".format(word, init_lives - lives))
    
    print("current state is: {}".format(guess))  

    show_rows = round((init_lives - lives) / init_lives * row_count)

    for i in range(0, show_rows -1 ):
        print(globals()[text_list[i]])

    n_attempt += 1
    if lives == 0 or guess.count("-") == 0 : break
    if n_attempt == attempts: print("you are out of attempts")
    
    
    
    
    







    
 













