
class KiloMan:

    def hitsTaken(self, pattern, jumps):

        hits = 0
        for idx, move in enumerate(jumps):
            height = pattern[idx]

            if(move == 'J' and height > 2):
                hits += 1
            elif(move == 'S' and height <= 2):
                hits += 1

        return hits
