
class StreetParking:
    
    def freeParks(self, street):
        
        parking = 0

        for idx, spot in enumerate(street):
            if(spot == '-'):
                bus = False
                side_street = False
                
                if((idx > 1 and street[idx - 1] == 'S') or (idx < len(street) - 1 and street[idx + 1] == 'S')):
                    side_street = True

                if((idx < len(street) - 2 and street[idx + 2] == 'B') or (idx < len(street) - 1 and street[idx + 1] == 'B')):
                    bus = True
                    
                if not bus and not side_street:
                    parking += 1
        return parking
