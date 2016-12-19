class Inchworm:
    
    def lunchtime(self, branch, rest, leaf):
        print(branch, rest, leaf)
            
        num_rests = branch / rest
        num_leaves = branch / leaf 
        
        eaten = 0
        
        for i in range(0, num_rests + 1):
            worm_pos = rest * i
            for j in range(0, num_leaves + 1):
                leaf_pos = j * leaf
                if(leaf_pos == worm_pos):
                    eaten += 1
        return eaten
