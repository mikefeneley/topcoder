import math

class RaceApproximator:

    def timeToBeat(self, d1, t1, d2, t2, raceDistance):

        time = t1 * math.exp( math.log(float(t2)/t1) * math.log(float(d1)/raceDistance) / math.log(float(d1)/d2) )
        
        time = int(time)
        hours = time / 3600
        minutes = (time - hours * 3600) / 60
        seconds = time - hours * 3600  - minutes * 60
        hours = str(hours)
        
        if(minutes < 10):
            minutes = '0' + str(minutes)
        else:
            minutes = str(minutes)

        if(seconds < 10):
            seconds = '0' + str(seconds)
        else:
            seconds = str(seconds)

        final = hours + ':' + minutes + ':' + seconds
        return final
