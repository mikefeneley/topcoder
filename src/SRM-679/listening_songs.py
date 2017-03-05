
class ListeningSongs:

    def listen(self, durations1, durations2, minutes, T):
        durations1 = list(durations1)
        durations2 = list(durations2)

        seconds = minutes * 60
        songs = 0
        for i in range(0, T):
            

            if len(durations1) <= 0 or len(durations2) <= 0:
                return -1

            first = min(durations1)
            second = min(durations2)
            seconds = seconds - first - second
            
            if seconds < 0:
                return -1

            durations1.remove(first)
            durations2.remove(second)
            songs += 2 
        
        comb = durations1 + durations2
        
        while len(comb) > 0 and seconds > 0:
            song = min(comb)
            seconds -= song
            
            if(seconds == 0):
                return songs + 1
            elif(seconds < 0):
                return songs
            else:
                songs += 1
            comb.remove(song)
        return -1
