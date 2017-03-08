
class LiveConcert:

    def maxHappiness(self, h, s):
        happy = 0
        done = []
        for idx, player in enumerate(s):
            if player not in done:
                index = []
                for i in range(idx, len(s)):
                    if s[i] == player:
                        index.append(i)
                        
                values = []
                for val in index:
                    values.append(h[val])
                happy += max(values)
                done.append(player)
        return happy
