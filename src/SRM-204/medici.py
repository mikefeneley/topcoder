
class Medici:

    def winner(self, fame, fortune, secrets):
        smallest = []
        
        for i in range(0, len(fame)):
            smallest.append(9999)

        for idx, val in enumerate(fame):
            if val < smallest[idx]:
                smallest[idx] = val
        for idx, val in enumerate(fortune):
            if val < smallest[idx]:
                smallest[idx] = val

        for idx, val in enumerate(secrets):
            if val < smallest[idx]:
                smallest[idx] = val
            
        greatest = max(smallest)
        times = 0
        index = -1
        for idx, val in enumerate(smallest):
            if greatest == val:
                times += 1
                index = idx
        if(times > 1):
            return -1
        else:
            return index
