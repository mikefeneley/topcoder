class Quipu:

    def readKnots(self, knots):
        i = 0
        num = ''
        while(i < len(knots)):
            
            counter = 0
            while(knots[i] == 'X'):
                counter += 1
                i += 1
            
            if(counter != 0):
                num = num + str(counter)
            
            counter = 0
            while(i < len(knots) and knots[i] == '-'):
                counter += 1
                i += 1
            for zeros in range(counter - 1):
                num = num + str(0)

        return num
