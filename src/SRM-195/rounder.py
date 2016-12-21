
class Rounder:

    def round(self, n, b):
        
        leftover = n % b
        if(leftover >= b/float(2)):
            tmp = n / b
            tmp = tmp * b
            tmp += b
        else:
            tmp = n / b
            tmp = tmp * b
        
        return tmp
