import copy

class SwapAndArithmetic:

    def able(self, x):
        elements = list(x)
        elements.sort()
        
        diff = elements[1] - elements[0]

        for i in range(0, len(elements) - 1):
            difference = elements[i + 1] - elements[i]
            if difference != diff:
                return "Impossible"
        return "Possible"
