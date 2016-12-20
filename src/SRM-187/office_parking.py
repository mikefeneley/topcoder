
class OfficeParking:

    def spacesUsed(self, events):
        spots = 0
        current = 0

        for event in events:
            div = event.split()
            
            if 'arrives' in div[1]:
                current += 1
                if(current > spots):
                    spots = current
            elif 'departs' in div[1]:
                current -= 1
        
        return spots
