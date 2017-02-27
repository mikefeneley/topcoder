
class SimilarUserDetection:

    def haveSimilar(self, handles):
        
        for idx, handle in enumerate(handles):
            remaining = handles[idx + 1:len(handles)]
            for comparison in remaining:
                if self.compare_handles(handle, comparison): 
                    return "Similar handles found"
            
        return "Similar handles not found"
    def compare_handles(self, first, second):
        
        print(first, second)
        
        if first == second:
            return True

        if len(first) != len(second):
            return False 

        similar = True
        for idx, char in enumerate(first):
            comp_char = second[idx:idx + 1]
            
            equal = False
            o_comp = False
            i_comp = False

            if char == comp_char:
                equal = True

            if (comp_char == 'O' or comp_char == '0') and (char == '0' or char == 'O'):
                o_comp = True

            if (comp_char == '1' or comp_char == 'l' or comp_char == 'I') and (char == 'I' or char == 'l' or char == '1'): 
                i_comp = True 
            
            if not equal and not o_comp and not i_comp:
                similar = False

        return similar
