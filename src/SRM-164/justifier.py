class Justifier:
    
    def justify(self, testIn):
        
        length = 0
        for name in testIn:
            if len(name) > length:
                length = len(name)

        names = []

        for name in testIn:
            num_spaces = length - len(name)
            padding = num_spaces * ' '
            name = padding + name
            names.append(name)
        return tuple(names)
