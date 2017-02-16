
class DoubleString:

    def check(self, s):
        first = s[0:len(s)/2]
        second = s[len(s)/2:len(s)]
        if first == second:
            return 'square'
        else:
            return 'not square'
