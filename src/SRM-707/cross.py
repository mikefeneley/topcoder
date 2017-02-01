
class Cross:

    def exist(self, board):
        print(board)
        
        first = board[0]
        length = len(first)
        height = len(board)

        for i in range(1, length - 1):
            for j in range(1, height - 1):
                top = board[i - 1]
                top = top[j]
                
                mid = board[i]
                mid = mid[j]
                
                bot = board[i + 1]
                bot = bot[j]
                
                left = board[i]
                left = left[j - 1]

                right = board[i]
                right = right[j + 1]

                if top == '#' and mid == '#' and bot == '#' and right == '#' and left == '#':
                    return "Exist"
        return "Does not exist"
