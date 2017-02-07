
class Ropestring:

    def makerope(self, s):
        total = len(s)
        indexable = list(s)        

        even = []
        odd = []
        final = []
        i = 0
        while i < len(indexable):
            string = ''
            while i < len(indexable) and indexable[i] == '-':
                string += '-'
                i += 1
            if string == '':
                i += 1
            elif len(string) % 2 == 0:
                even.append(string) 
            elif len(string) % 2 == 1:
                odd.append(string)
        
        even.sort(reverse=True)
        odd.sort(reverse=True)
        
        string = ''
        for rope in even:
            string += rope + '.'
        for rope in odd:
            string += rope + '.' 

        bot = len(string)
        if bot > total:
            string = string[0:len(string) - 1]
            return string
        for i in range(bot, total):
           string += '.' 
        return string
