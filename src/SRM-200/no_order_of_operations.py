
class NoOrderOfOperations:

    def evaluate(self, expr):
        
        hold = expr
        hold = hold.replace('*', '+')
        hold = hold.replace('-', '+')
        hold = hold.replace('/', '+')
        nums = hold.split('+')
        
        hold = expr

        for i in range(0, 10):
            hold = hold.replace(str(i), ',')
        hold = hold.split(',')
        ops = [x for x in hold if x]
        nums = map(int, nums)


        num = nums[0]
        for idx, op in enumerate(ops):
            if('+' in op):
                result = num + nums[idx + 1]
            if('-' in op):
                result = num - nums[idx + 1]
            if('*' in op):
                result = num * nums[idx + 1]
            if('/' in op):
                result = float(num) / nums[idx + 1]
            num = result

        return num
