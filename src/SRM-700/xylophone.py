
class Xylophone:

    def countKeys(self, keys):
        
        result = [0, 0, 0, 0, 0, 0, 0]
        for key in keys:
            index = (key - 7) % 7
            result[index] += 1

        distinct = 0
        for idx, key in enumerate(result):
            if(key > 0):
                distinct += 1
        return distinct
