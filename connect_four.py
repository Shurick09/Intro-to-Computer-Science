'''
Created on May 2, 2017

@author: Shurick

Alex Rozenblit

I pledge my honor that I have abided by the Stevens Honor Code.
'''

class Board(object):
    '''A user-defined data structure that represents a connect four board.'''
    
    def __init__(self, width=7, height=6):
        '''The constructor for Board'''
        self.width = width
        self.height = height
        w = self.width
        h = self.height
        self.board=[[" "]*w for _ in range(h)]
        
    def __str__(self):
        '''Prints the Board'''
        s = ''
        for i in range(self.height):
            for x in range(self.width):
                s = s + '|' + self.board[i][x]
            s = s + '\n'
        s = s + self.width * '-'
        s = s + '\n'
        for a in range(self.width):
            s = s + '' + str(a)
        return s
 
    def allowsMove(self,col):
        '''Returns true if the player can make a move in column col'''
        if col < 0 or col >= self.width:
            return False
        for i in range(self.height):
            if self.board[i][col] != '':
                return False
        return True
    
    def addMove(self,col,ox):
        '''Adds variable ox to the highest row number in column col'''
        for x in range(self.height - 1, -1, -1):
            if self.board[x][col] == '':
                self.board[x][col] = ox
                return
                
                
    def setBoard( self, moveString ):
        ''' takes in a string of columns and places
         alternating checkers in those columns,
         starting with 'X'
         
         For example, call b.setBoard('012345')
         to see 'X's and 'O's alternate on the
         bottom row, or b.setBoard('000000') to
         see them alternate in the left column.
         
          moveString must be a string of integers''' 
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': 
                nextCh = 'O'
            else:
                nextCh = 'X'
        
    def delMove(self,col):
        '''Removes the top checker from column col'''
        for i in range(self.height-1,-1):
            if self.board[i][col] != '':
                self.board[i][col] = ''
        
    def winsFor(self, ox):
        for i in range(self.height):
            for j in range(self.width-3):
                if self.board[i][j]==ox and self.board[i][j+1]==ox and self.board[i][j+2]==ox and self.board[i][j+3]==ox:
                    return True 
        for i in range(self.height-3):
            for j in range(self.width):
                if self.board[i][j]==ox and self.board[i+1][j]==ox and self.board[i+2][j]==ox and self.board[i+3][j]==ox:
                    return True
        for i in range(self.height-3):
            for j in range(self.width-3):
                if self.board[i][j]==ox and self.board[i+1][j+1]==ox and self.board[i+2][j+2]==ox and self.board[i+3][j+3]==ox:
                    return True
        i=self.height-1
        j=self.width-1
        while i>2:
            while j>2:
                if self.board[i][j]==ox and self.board[i-1][j-1]==ox and self.board[i-2][j-2]==ox and self.board[i-3][j-3]==ox:
                    return True
                j-=1
            i-=1
        return False
        
    def hostGame(self):
        '''Runs the game'''
        print('Welcome to Connect 4!')
        print(self)
        while True:
            col = -1
            while self.allowsMove(col) == False:
                col = int(input('X: Choose a column: '))
            self.addMove(col, 'X')
            print(self)
            if self.winsFor('X'):
                print('X Wins')
                return None
            col = -1
            while self.allowsMove(col) == False:
                col = int(input('O: Choose a column: '))
            self.addMove(col, 'O')
            print(self)
            if self.winsFor('O'):
                print('O Wins')
                return None
                
if __name__ == '__main__':       
    b = Board()
    b.hostGame()
