class Board:
    def __init__(self):
        self.grid=[[' ' for col in range(3)] for row in range(3)]

    def print_board(self):
        for row in self.grid:
            print(' | '.join(row))
    
    def is_full(self):
        return all([col!=' ' for row in self.grid for col in row])
    
    def is_cell_empty(self,x,y):
        return self.grid[x][y]==' '
    
    def set_cell(self,x,y,symbol):
        if not self.is_cell_empty(x,y):
            return False
        self.grid[x][y]=symbol
        return True
    
    def reset_cell(self,x,y):
         self.grid[x][y]=' '

    def get_empty_cells(self):
         return [(i,j) for i in range(3) for j in range(3) if self.grid[i][j]==' ']
    
    def evluate(self,ai_symbol,human_symbol):
        for i in range(3):
            if self.grid[i][0]==self.grid[i][1]==self.grid[i][2]!=' ':
                return 10 if self.grid[i][0]==ai_symbol else -10
            if self.grid[0][i]==self.grid[1][i]==self.grid[2][i]!=' ':
                return 10 if self.grid[1][i]==ai_symbol else -10
            
        if self.grid[0][0]==self.grid[1][1]==self.grid[2][2]!=' ':
                return 10 if self.grid[0][0]==ai_symbol else -10 
        if self.grid[0][2]==self.grid[1][1]==self.grid[2][0]!=' ':
                return 10 if self.grid[1][1]==ai_symbol else -10
        
        return 0
    
    