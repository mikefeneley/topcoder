
class LetterStrings:

    def sum(self, s):
        total = 0
        for string in s:
            for letter in string:
                if(letter != '-'):
                    total += 1
        return total
