
class MagicSquare:

    def missing(self, square):
        val = -1

        for idx, num in enumerate(square): 
            if(num == -1):
                for i in range(1, 100):
                    tmp = list(square)
                    tmp[idx] = i
                    correct = self.verify(tmp)
                    if(correct):
                        return i 

    def verify(self, square):

        first = 0
        second = 0
        third = 0

        for i in range(0, 3):
            first += square[i]
        for j in range(3, 6):
            second += square[j]
        for k in range(6, 9):
            third += square[k]

        print(first, second, third)

        if(first != second or first != third or second != third):
            return False
        else:
            return True
