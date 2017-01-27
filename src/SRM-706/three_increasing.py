
class ThreeIncreasing:

    def minEaten(self, a, b, c):
       
        candies_eaten = 0
        
        while(c <= b):
            b -= 1
            candies_eaten += 1
        while(b <= a):
            a -= 1
            candies_eaten += 1

        if(a <= 0 or b <= 0 or c <= 0):
            return -1
        else:
            return candies_eaten
