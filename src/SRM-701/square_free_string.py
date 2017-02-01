
class SquareFreeString:

    def isSquareFree(self, s):
        for i in range(0, len(s)):
            for length in range(1, len(s)):
                first = s[i:length + i]
                second = s[i+length:i+length+length] 
                if second == first:
                    return "not square-free"
        return "square-free"
