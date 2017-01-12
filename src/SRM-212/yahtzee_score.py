
class YahtzeeScore:

    def maxPoints(self, toss):
        max_val = 0

        for i in range(1, 7):
            total = 0
            for val in toss:
                if val == i:
                    total += val
            
            if(total > max_val):
                max_val = total
        return max_val
