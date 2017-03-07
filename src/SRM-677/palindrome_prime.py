
class PalindromePrime:

    def count(self, L, R):
        num = 0
        for i in range(L, R + 1):
            if self.isPalindromePrime(i) and not i is 1:
                print(i)
                num += 1

        return num
    def isPalindromePrime(self, num):
        
        for i in range(2, num):
            if num % i == 0:
                return False

        str_num = str(num)
        length = len(str_num)
        
        if length % 2 == 0:
            first = str_num[0:len(str_num) / 2]
            second = str_num[len(str_num) / 2: len(str_num)]
            return first == second
        else:
            first = str_num[0:len(str_num) / 2]
            second = str_num[len(str_num) / 2 + 1: len(str_num)]
            return first == second
