
class TriangleMaking:

    def maxPerimeter(self, a, b, c):
        first = a
        second = b
        third = c

        sides = [first, second, third]

        for idx, side in enumerate(sides):
            one = (idx + 1) % 3
            two = (idx + 2) % 3

            total = sides[one] + sides[two]
            while sides[idx] >= total:
                sides[idx] -= 1
                
        return sum(sides)
