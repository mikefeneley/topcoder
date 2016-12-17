class FixedPointTheorem:
    def cycleRange(self, R):
    	x = 0.25
    	high = -1
        low = 999
        for i in range(0, 201001):
            x = R * x * (1-x)

            if(i > 200000):

                if(x > high):
                    high = x
                if(x < low):
                    low = x
        return high - low