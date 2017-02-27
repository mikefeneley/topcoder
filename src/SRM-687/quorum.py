
class Quorum:

    def count(self, arr, k):
        arr = list(arr)
        total = 0

        for i in range(0, k):
            amount = min(arr)
            arr.remove(amount)
            total += amount
        return total
