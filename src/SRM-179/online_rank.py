
class OnLineRank:

    def calcRanks(self, k, scores):
        ranks = 0  

        for idx, score in enumerate(scores):
            counter = k - 1
            new_ranks = 1
        
            while(counter > 0):
                if(idx - counter >= 0 and score > scores[idx - counter]):
                    new_ranks += 1
                counter -= 1
            ranks += new_ranks
        
        return ranks
