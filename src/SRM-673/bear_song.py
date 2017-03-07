
class BearSong:

    def countRareNotes(self, notes):
        this = {}
        
        for note in notes:
            if note not in this:
                this[note] = 1
            else:
                this[note] += 1

        unique = 0
        for note in this:
            if this[note] == 1:
                unique += 1
        return unique
