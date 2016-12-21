
class Multiples:

    def number(self, min, max, factor):
        num = 0
        for i in range(min, max + 1):
            if i % factor == 0:
                num += 1
        return num
