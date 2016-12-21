import math

class Bits:

    def minBits(self, n):
        for i in range(0, 20):
            val = math.pow(2, i)
            
            if val > n:
                return i
