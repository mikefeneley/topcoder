
class CutoffRounder:

    def round(self, num, cutoff):
        div = num.split('.')
       
        if(len(div) == 1):
            return div[0]
        
        if(div[0] == ''):
            num = 0
        else:
            num = float(div[0])

        if(div[1] == ''):
            dec = 0
        else:
            dec = float('0.' + div[1])
        
        cutoff = float(cutoff)
       
        if dec < cutoff:
            return num
        else:
            return num + 1
