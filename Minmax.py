import math
class Minmax:
    def __init__(self,ai_symbol,human_symbol):
        self.ai_symbol=ai_symbol
        self.human_symbol=human_symbol


    def minmax(self,grid,ai_turn,alpha,beta):
        score=grid.evluate(self.ai_symbol, self.human_symbol)
        if score==10 or score==-10:
            return score
        if grid.is_full():
            return 0
        best_score=0
        if ai_turn:
            best_score=-math.inf
            for i,j in grid.get_empty_cells():
                grid.set_cell(i,j,self.ai_symbol)
                best_score=max(best_score,self.minmax(grid,False,alpha,beta))
                grid.reset_cell(i,j)
                alpha=max(alpha,best_score)
                if beta<=alpha:
                    break
        else:
            best_score=math.inf
            for i,j in grid.get_empty_cells():
                grid.set_cell(i,j,self.human_symbol)
                best_score=min(best_score,self.minmax(grid,True,alpha,beta))
                grid.reset_cell(i,j)
                beta=min(beta,best_score)
                if beta<=alpha:
                    break
        return best_score
         

    def get_best_move(self,grid):
        best_score=-math.inf
        best_cordi=(-1,-1)
        for i,j in grid.get_empty_cells():
            grid.set_cell(i,j,self.ai_symbol)
            score=self.minmax(grid,False,-math.inf,math.inf)
            if score>best_score:
                best_score=score
                best_cordi=(i,j)
            grid.reset_cell(i,j)
        return best_cordi
        