import itertools
import math

class MultiplicationTable2Easy:

    def isGoodSet(self, table, t):
        total = len(table)
        n = int(math.log(total, 2))
        perm = itertools.product(t, repeat=2)

        for prod in perm:
            i = prod[0]
            j = prod[1]
            index = i * n + j
            table_val = table[index]

            if table_val not in t:
                return "Not Good"
        return "Good"
