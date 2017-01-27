
class AlternatingString:

    def maxLength(self, s):
        maxlen = 0

        for i in range(0, len(s)):
            prev = i
            count = 1 
            for j in range(i + 1, len(s)):
                if s[prev] != s[j]:
                    count += 1
                    prev += 1
                else:
                    break
            if(count > maxlen):
                maxlen = count
        return maxlen
