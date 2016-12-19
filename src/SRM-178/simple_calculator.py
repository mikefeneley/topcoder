
class SimpleCalculator:

    def calculate(self, input):
        add = False
        sub = False
        mul = False
        div = False

        for char in input:
            if char == '+':
                add = True
            if char == '-':
                sub = True
            if char == '*':
                mul = True
            if char == '/':
                div = True
        
        input = input.replace('+', ' ')
        input = input.replace('/', ' ')
        input = input.replace('*', ' ')
        input = input.replace('-', ' ')

        vals = input.split()
        first = int(vals[0])
        second = int(vals[1])

        if add:
            result = first + second
        if sub:
            result = first - second
        if mul:
            result = first * second
        if div:
            result = first / second

        return result
