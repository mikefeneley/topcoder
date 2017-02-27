
class StepsConstruct:

    def construct(self, board, k):
        self.board = board
        self.k = k
        self.height = len(board)
        self.width = len(board[0])
        self.final = (self.width - 1, self.height - 1) 
        print(self.final)
        self.moves = ['B']
        self.move = [(0, 0)]
        self.make_move()

    def make_move(self): 
        pos = self.move[len(self.move) - 1] 
        x = pos[0]
        y = pos[1]
        print("CURRENT_POS", pos, "FULL", self.move, "MOVE", self.moves) 
        right_move = (x + 1, y)
        left_move = (x - 1, y)
        up_move = (x, y - 1)
        down_move = (x, y + 1)
       
        print(pos, self.final, "TEST")
        if(pos == self.final):
            print("SAT", self.moves, self.move) 
            if(len(self.moves) <= self.k):
                print("SAT", self.moves, self.move) 
                return True 
        # Try Right
        if right_move not in self.move and (x + 1) < self.width: 
            self.move.append(right_move)
            self.moves.append("R")
            self.make_move()
            
        if down_move not in self.move and (y + 1) < self.height: 
            self.move.append(down_move)
            self.moves.append("D")
            self.make_move()
#        if left_move not in self.move and (x - 1) > 0: 
#            self.move.append(left_move)
#            self.moves.append("L")
#            self.make_move()
#        if up_move not in self.move and (y - 1) > 0: 
#            self.move.append(up_move)
#            self.moves.append("U")
#            self.make_move()
        self.move.pop() 
        self.moves.pop()
        print("AFTER", self.moves)
a = StepsConstruct()

b = (".#...",
         ".#.#.",
          ".#.#.",
           ".#.#.",
            "...#.")



a.construct(b, 4)
