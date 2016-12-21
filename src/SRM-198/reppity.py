
class Reppity:

    def longestRep(self, input):
        longest = 0
        for idx, char in enumerate(input):
            
            string = char
            length = 1
            counter = 1
            while string in input[idx + counter:len(input)] and idx + counter < len(input):
                
                if(longest < length):
                    longest = length

                string += input[idx + counter] 
                
                counter += 1
                length += 1
        
        return longest
