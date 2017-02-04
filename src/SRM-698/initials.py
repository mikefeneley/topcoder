
class Initials:

    def getInitials(self, name):
        blocks = name.split(" ")
        init = ""

        for block in blocks:
            letter = block[0:1]
            init += letter
        return init
