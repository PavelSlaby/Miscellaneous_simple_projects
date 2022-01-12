# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 23:02:37 2022

@author: pavel
"""
class board():
     
    def __init__(self, n_col = 8, n_let = 8):
        self.help = """
                    This creates a board for any game like tick-tack-toe, chess etc.
                    """
       
        self.n_col = n_col
        self.n_let = n_let
        self.clean_board = str()
        self.all_positions = []
        self.current_board = str()
         
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


a = board()
a.intro()
a.show_board()
print(a.prepare_board())

        