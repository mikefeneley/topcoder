
class CountGame:

    def howMany(self, maxAdd, goal, next):
        
       
        for i in range(next, next + maxAdd):
            perfect_game = self.check_win(maxAdd, goal, next, i)

            if(perfect_game):
                return i

            
        




        
        

    def check_win(self, maxAdd, goal, next, val):
        
        loss = False
        
        # 1 = Opponent, 0 Player
        players_turn = 1

        
            





a = CountGame()
b = 3
c = 20
d = 10
a.howMany(b, c, d)
