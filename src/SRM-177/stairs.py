
class Stairs:

    def designs(self, maxHeight, minWidth, totalHeight, totalWidth):
        
        width_combos = 0
        height_combos = 0
        combo = 0

        for height in range(1, maxHeight + 1):
            risers = totalHeight / height
            treads = risers -  1
            if(treads != 0):
                width = totalWidth / treads

            if(width >= minWidth and height *  risers == totalHeight and width * treads == totalWidth):
                combo += 1
        
        return combo 
