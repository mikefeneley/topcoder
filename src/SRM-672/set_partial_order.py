
class SetPartialOrder:

    def compareSets(self, a, b):
        
        if len(a) == len(b) :
            for element in a:
                if element not in b:
                    return "INCOMPARABLE"
            return "EQUAL"
        elif len(a) < len(b): 
            for element in a:
                if element not in b:
                    return "INCOMPARABLE"
            return "LESS"
        else:
            for element in b:
                if element not in a:
                    return "INCOMPARABLE"
            return "GREATER"
