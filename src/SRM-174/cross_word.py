
class CrossWord:

    def countWords(self, board, size):
        
        num_slots = 0
        for row in board:
            div = row.split("X")
            
            for slot in div:
                if(len(slot) == size):
                    num_slots += 1

        return num_slots
