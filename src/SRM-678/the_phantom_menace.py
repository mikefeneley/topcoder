
class ThePhantomMenace:

    def find(self, doors, droids):
        greatest_min = -1 
        best_door = doors[0]
        for idx, door in enumerate(doors):
            greatest_distance = 9999 
            for droid in droids:
                distance = abs(droid - door)
                if distance < greatest_distance:
                    greatest_distance = distance
            
            

            if greatest_distance > greatest_min:
                greatest_min = greatest_distance
            
        return greatest_min
