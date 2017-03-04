
class BearPair:

    def bigDistance(self, s):
        i = 0
        j = len(s) - 1
        
        num = 0

        first = s[i]
        second = s[j]
        while j > 0 and s[j] == first:
            j -= 1
        first_result = abs(i - j)

        j = len(s) - 1
        while i < len(s) - 1 and s[i] == second:
            i += 1
        
        second_result = abs(i - j)

        if first_result == 0 and second_result == 0:
            return -1
        else:
            return(max(first_result, second_result))
