
class Average:

    def belowAvg(self, math, verbal):
        composites = []

        for val in math:
            composites.append(val)

        for idx, val in enumerate(verbal):
            composites[idx] += val

        average = sum(composites) / float(len(composites))

        below = 0
        for score in composites:
            if(score < average):
                below += 1
        return below
