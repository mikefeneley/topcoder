
class Soccer:

    def maxPoints(self, wins, ties):
        points = []

        for idx, win in enumerate(wins):
            points.append(win * 3)
            points[idx] += ties[idx]
        
        return max(points)
