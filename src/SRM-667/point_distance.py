
class PointDistance:

    def findPoint(self, x1, y1, x2, y2):
        x = 0
        y = 0
            
        if x2 > x1 and x2 < 100:
            x = 100
        elif x1 > x2 and x2 > -100:
            x = -100
        else:
            x = x2

        if y2 > y1 and y2 < 100:
            y = 100
        elif y1 > y2 and y2 > -100:
            y = -100
        else:
            y = y2
        return (x, y)

