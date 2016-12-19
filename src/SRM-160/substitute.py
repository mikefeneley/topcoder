class Substitute:
    def getValue(self, key, code):
        val = ''
        for char in code:
            for idy, letter in enumerate(key):
                if(char == letter):
                    num = (idy + 1)%10
                    val += str(num) 
        return val
