# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 17:28:48 2022

## Game of Tick Tack Toe

@author: pavel slaby
"""

##libraries


simple_board = """
      
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
print(simple_board)


class TickTack():
     
    def __init__(self, n_col = 3, n_let = 3):
        self.help = """
                    This is a game of Tick-Tack-Toe
                    When asked, input the position on the board, where you want to place your X / O
                    
                    Good luck :-) 
                    """
       
        self.n_col = n_col
        self.n_let = n_let
        self.clean_board = str()
        self.all_positions = []
        self.moves_hist = {}
        self.current_board = str()
        self.__removed = []
         
        import string
        self.letters = string.ascii_uppercase

        # get the list of possible positions
        for l in self.letters[:self.n_let]:
            for i in range(1,  self.n_col + 1):
                self.all_positions.append( str(i) + l   )
    
    def prepare_board(self, clean = None):
       
        string = " " * 4

        for i in range(1, self.n_col + 1):
            string = string  + str(i) + " " * 4

        string += '\n'
        string += '__|' + '____|' * (self.n_col) + "_"


        string += '\n'


        for L in self.letters[:self.n_let]:
            
            string += '  |' + '    |' * (self.n_col)
            string += '\n'
            
            string += L + " |"
            
            for i in range(1, self.n_col + 1):
                string += " " + str(i) + L + " |"    
            
            string += '\n'
            string += '__|' + '____|' * (self.n_col) + "_"
            
            string += '\n'

        string += '  |' + '    |' * (self.n_col)
        
        if clean == True:
            # clean the board print   
            self.clean_board = string
            
            for i in range( 0, len(self.all_positions)):
                self.clean_board = self.clean_board.replace(self.all_positions[i] , "  ")
            return self.clean_board
        else:  
            return string
    
    def show_board(self):
        print(self.prepare_board(1==1))
    
    
    def intro(self):
       print(self.help)
       self.show_board()
       
    def move(self, x, p, moves_hist = {}):
       #x is the position on the board
       #p is the player number
       
       if x not in self.all_positions:
           print("Wrong input, you can only input one of the following positions: " + str(self.all_positions))
        
       elif x in self.moves_hist:
           print("Wrong input, you can only input a position that was not entered before: " + str(list(set(self.all_positions).difference(set(self.moves_hist)))))
               
       else:
                  
           self.current_board = self.prepare_board(False) 
           single_position = self.all_positions.copy()
           
           self.__removed.append(x)
           
           for i in self.__removed: single_position.remove(i)
                       
           for i in range( 0, len(single_position)):
               self.current_board = self.current_board.replace(single_position[i] , "  ")
            
           moves_hist[x] = p    
            
           for move, player in moves_hist.items():
               if player == 1:
                   tick = " X"
               else:
                   tick = " O"
                   
               self.current_board = self.current_board.replace(move , tick)
    
           print(self.current_board)
           self.moves_hist = moves_hist
        
        
    def history(self):
        print(self.__moves_hist)
        
    
a = TickTack()
a.all_positions
a.prepare_board()
a.show_board()
a.intro()

a.move('1B', 1 )
a.move('3A', 2 )
a.move('1B', 1 )


