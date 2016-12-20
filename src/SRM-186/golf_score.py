
class GolfScore:

    def tally(self, parValues, scoreSheet):
        
        strokes = 0
        for idx, par in enumerate(parValues):
            result = scoreSheet[idx]
            
            if("triple bogey" in result):
                score = par + 3
            elif("double bogey" in result):
                score = par + 2
            elif("bogey" in result):
                score = par + 1
            elif("par" in result):
                score = par
            elif("birdie" in result):
                score = par - 1
            elif("eagle" in result):
                score = par - 2
            elif("albatross" in result):
                score = par - 3
            elif("hole in one" in result):
                score = 1
            strokes += score
        
        return strokes
