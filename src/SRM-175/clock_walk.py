
class ClockWalk:

    def finalPosition(self, flips):
        counter = 0

        for idx, char in enumerate(flips):
            move = (idx + 1)
            if char == 'h':
                counter += move 
            elif char == 't':
                counter -= move
        hours = ((counter % 12) + 12) % 12
        
        if hours == 0:
            return 12
        else:
            return hours
