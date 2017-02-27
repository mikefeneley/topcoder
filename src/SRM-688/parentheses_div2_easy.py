
class ParenthesesDiv2Easy:

    def getDepth(self, s):
        max_depth = 0
        tmp_depth = 0
        for char in s:
            if char == '(':
                tmp_depth += 1
                if tmp_depth > max_depth:
                    max_depth = tmp_depth
            elif char == ')':
                tmp_depth -= 1
        return max_depth

