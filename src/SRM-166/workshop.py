import itertools 

class Workshop:
    
    def pictureFrames(self, pieces):
        num_pictures = 0
        
        results = itertools.combinations(pieces, 3)
        
        for result in results:
            piece1 = result[0]
            piece2 = result[1]
            piece3 = result[2]

            first = piece2 + piece3
            second = piece1 + piece3
            third = piece1 + piece2

            if(first > piece1 and second > piece2 and third > piece3):
                num_pictures += 1
        return num_pictures
