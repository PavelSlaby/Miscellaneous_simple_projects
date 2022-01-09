# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 17:28:48 2022

## Game of Tick Tack Toe

@author: pavel
"""

##libraries
import string



n = 3 #the number of columns
d = 'C' # letter of the last row

full_board = """
      
                    1     2     3
              ___|_____|_____|_____|_  
                 |     |     |     |
              A  | 1A  |  2A |  3A |
              ___|_____|_____|_____|_
                 |     |     |     |
              B  | 1B  |  2B |  3B |
              ___|_____|_____|_____|_
                 |     |     |     |
              C  | 1C  |  2C |  3C |
              ___|_____|_____|_____|_
                 |     |     |     |
"""


letters = string.ascii_uppercase
all_positions = []

# get the list of possible positions
for l in range(0, letters.find(d) + 1):
    for i in range(1,  n + 1):
        all_positions.append( str(i) + letters[l]   )


# show the board


intro_text = """
            This is a game of Tick Tack Toe
            The board is showed below.
            When asked, input the position on the board, where you want to place your X / O
            
            Good luck :-) 
"""


clean_board = full_board    

# clean the board print    
for i in range( 0, len(all_positions)):
    clean_board = clean_board.replace(all_positions[i] , "  ")

print(intro_text)
print(clean_board)


p1 = "Player 1, it is your turn:"

#move = input(p1)
# make some error handling if not inputed correctly



## Initialization
single_position = all_positions.copy()
current_board = full_board
removed = []
moves_hist = {}

# make a move
def move(x, p, moves_hist):
    #x is the position on the board
    #p is the player number
    current_board = full_board    
    single_position = all_positions.copy()
    
    removed.append(x)
    
    for i in removed: single_position.remove(i)
                
    for i in range( 0, len(single_position)):
        current_board = current_board.replace(single_position[i] , "  ")
     
    moves_hist[x] = p    
     
    for move, player in moves_hist.items():
        if player == 1:
            tick = " X"
        else:
            tick = " O"
            
        current_board = current_board.replace(move , tick)

    print(current_board)

    return moves_hist


x = '3B'
p = 2

moves_hist = move("3B", 2, moves_hist)

moves_hist = move("1A", 1, moves_hist)

moves_hist = move("1B", 2, moves_hist)



x = '2C'
p = 1

move("2C", 1)




print(full_board)

single_position = all_positions
    


#make a move
# 2B
clean_board = full_board  
single_position = all_positions
single_position.remove("2B")

for i in range( 0, len(single_position)):
    clean_board = clean_board.replace(single_position[i] , "  ")

clean_board = clean_board.replace("2B" , "X ")

print(clean_board)





print(clean_board)


move = input("whats your next move?")


print(
      board.replace("1A", " X")
      )







