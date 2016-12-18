class TireRotation:
        
    def getCycle(self, initial, current):
        first = initial
        second = initial[3] + initial[2] + initial[0] + initial[1]
        third = initial[1] + initial[0] + initial[3] + initial[2]
        fourth = initial[2] + initial[3] + initial[1] + initial[0]

        if(current == first):
            return 1
        if(current == second):
            return 2
        if(current == third):
            return 3
        if(current == fourth):
            return 4
        return -1
