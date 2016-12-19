class LCMRange:
    def lcm(self, first, last):
        small = 1
        while(1):
            divisable = True
            for i in range(first, last + 1):
                if(small % i != 0):
                    divisable = False

            if(divisable):
                return small
            else:
                small += 1
