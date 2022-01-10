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



p1 = "Player 1, it is your turn:"
p2 = "Player 2, it is your turn:"


move = input(p1)
# make some error handling if not inputed correctly




x = '3B'
p = 2

moves_hist = move("3B", 2, moves_hist)
moves_hist = move("1A", 1, moves_hist)
moves_hist = move("1B", 2, moves_hist)



class TickTack():
     
    def __init__(self, n = 3, d = 'C'):
        self.help = """
                    This is a game of Tick-Tack-Toe
                    The board is showed below.
                    When asked, input the position on the board, where you want to place your X / O
                    
                    Good luck :-) 
                    """
        self.n = n
        self.d = d
        self.full_board = """
      
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
        
        
        import string
        import sys 
        
        self.__letters = string.ascii_uppercase
        self.__all_positions = []

        # get the list of possible positions
        for l in range(0, self.__letters.find(self.d) + 1):
            for i in range(1,  self.n + 1):
                self.__all_positions.append( str(i) + self.__letters[l]   )

        self.__clean_board = self.full_board    

        # clean the board print    
        for i in range( 0, len(self.__all_positions)):
            self.__clean_board = self.__clean_board.replace(self.__all_positions[i] , "  ")


        self.__single_position = self.__all_positions.copy()
        self.current_board = self.full_board
        self.__removed = []
        self.__moves_hist = {}
    
    
    
    def intro(self):
       print(self.help)
       print(self.__clean_board)

 
    def move(self, x, p, moves_hist = {}):
       #x is the position on the board
       #p is the player number
       
       if x not in self.__all_positions:
           print("Wrong input, you can only input one of the following positions: " + str(self.__all_positions))
        
       elif x in self.__moves_hist:
           print("Wrong input, you can only input a position that was not entered before: " + str(list(set(self.__all_positions).difference(set(self.__moves_hist)))))
               
       else:
                  
           self.current_board = self.full_board    
           self.__single_position = self.__all_positions.copy()
           
           self.__removed.append(x)
           
           for i in self.__removed: self.__single_position.remove(i)
                       
           for i in range( 0, len(self.__single_position)):
               self.current_board = self.current_board.replace(self.__single_position[i] , "  ")
            
           moves_hist[x] = p    
            
           for move, player in moves_hist.items():
               if player == 1:
                   tick = " X"
               else:
                   tick = " O"
                   
               self.current_board = self.current_board.replace(move , tick)
    
           print(self.current_board)
           self.__moves_hist = moves_hist
        
        
    def history(self):
        print(self.__moves_hist)
        
        
n = 3 #the number of columns
d = 'C' # letter of the last row

a = TickTack()
print(a.help)
print(a.full_board)
a.intro()
a.history()

a.move('1B', 1 )
a.move('3A', 2 )


p = '2B'

if len(p) != 2 or p[0].isalpha() or p[1].isdigit():
    print('error')


moves_hist
all_positions.sort()




a.n
a.d

