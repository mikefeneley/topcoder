
class StringMult:

    def times(self, sFactor, iFactor):

        if(sFactor == ""):
            return ""
        elif(iFactor == 0):
            return ""
        elif(iFactor > 0):
            return sFactor * iFactor
        else:
            reverse = sFactor[::-1]
            return reverse * abs(iFactor)
