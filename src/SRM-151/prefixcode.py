class PrefixCode:

    def isOne(self, words):
        for word in words:
            for check in words:
                prefix = check[0:len(word)]
                if word == prefix:
                    return True
        return False
