
class RGBColor:

    def getComplement(self, rgb):
        
        comp = [] 
        
        for color in rgb:
            complement = 255 - color
            if(abs(color - complement) <= 32):
                if(color <= 128):
                    complement  = color + 128
                else:
                    complement = color - 128
           
            comp.append(complement)
        print(comp) 
        return tuple(comp)
