
class TitleString:
       
    def toFirstUpperCase(self, title):
            
        new_word = ""
        i = 0
        while(i < len(title)):
            char = title[i]
            print(char, "AJSDKLAS")
            if(char.isalpha()):
                char = char.upper()
            new_word = new_word + char
            i += 1            

            while(i < len(title) and title[i] != ' '):
                print(title[i], "HERE")
                new_word = new_word + title[i]
                i += 1
            i += 1
            if(i < len(title)):
                new_word = new_word + " "
        print(new_word)
        return new_word
        
        
        
a = TitleString()
a.toFirstUpperCase("intro to algorithims")

