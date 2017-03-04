
class DNASequence:

    def longestDNASequence(self, sequence):
        longest = 0
        new = 0
        for char in sequence:
            if char == 'A' or char == 'C' or char == 'G' or char == 'T':
                new += 1
                longest = max(longest, new)
            else:
                new = 0
        return longest
         
