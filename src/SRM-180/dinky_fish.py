
class DinkyFish:

    def monthsUntilCrowded(self, tankVolume, maleNum, femaleNum):
        
        months = 0
        while(1):
           
            total = sum((maleNum, femaleNum))
            space = tankVolume/float(total)
            
            if(space < 0.5):
                return months
    
            couples = min((maleNum, femaleNum))
            maleNum += couples
            femaleNum += couples
            months += 1
