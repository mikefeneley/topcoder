
class SkipRope:

    def partners(self, candidates, height):
        
        first = (-1, 200)
        second = (-1, 200)

        for idx, person in enumerate(candidates):
            diff = abs(person - height)
     
            if diff < abs(first[1] - height):
                first = (idx, person)
            elif diff == abs(first[1] - height) and person > first[1]:
                first = (idx, person)

        for idx, person in enumerate(candidates):
            
            if(idx != first[0]):
            
                diff = abs(person - height)
                old_diff = abs(second[1] - height) 
                
                if diff < old_diff:
                    second = (idx, person)
                elif diff == abs(second[1] - height) and person > second[1]:
                    second = (idx, person)
        
        closest = (first[1], second[1])
        closest = sorted(closest) 
        return closest
