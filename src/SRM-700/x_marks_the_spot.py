import time

import math

import copy

import sys


QUESTION = 63

DOT = 46

SPOT = 79


class XMarksTheSpot:


    def __init__(self):

        pass


    def generate_combination(self, board_num, total_boards):

        #print "\n\ngenerate_combination", board_num, total_boards

        format_spec =  '0' + str(total_boards) + 'b'         

        binary_combination = format(board_num, format_spec) 

        #print "BINARY COMBINATION", binary_combination

        return binary_combination 


    def generate_map(self, comb, base_map):

        comb_index = 0

        for idy, line in enumerate(base_map):

            for idx, hex_char in enumerate(line):

                if hex_char == QUESTION:

                    new_char = DOT if int(comb[comb_index]) else SPOT

                    base_map[idy][idx] = new_char 

                    comb_index += 1

        return base_map


    def count_locations(self, comb_map):

        #print "\n\ncount_locations" 

        #for line in comb_map:

        #    print line


        top = sys.maxsize

        left = sys.maxsize

        bot = -1

        right = -1


        for idy, line in enumerate(comb_map):

            #print "LINE"

            #print "SPOT IN LINE", SPOT in line

            if SPOT in line and idy < top:

                top = idy

            if SPOT in line and idy > bot:

                bot = idy 


            for idx, hex_char in enumerate(line):

                if hex_char == SPOT and idx < left:

                    left = idx

                if hex_char == SPOT and idx > right:

                    right = idx

               

        height = abs(top - bot) + 1

        width = abs(left - right) + 1


        #print "TOP", top, "LEFT", left, "RIGHT", right, "BOT", bot

        height = 1 if not height else height

        width = 1 if not width else width

        #print "HEIGHT, WIDTH",  height, width


        options = height * width

        #print "OPTIONS", options

        return options

    

    def countArea(self, board):


        for idx, line in enumerate(board):

            board[idx] = bytearray(line)

        

        num_boards = 0

        

        for line in board:

            num_boards += line.count('?')

       

        if num_boards == 0:

            total_boards = 1

        else:

            total_boards = 2 << (num_boards -1)


        total_locations = 0 

        for i in range(0, total_boards):

            comb = self.generate_combination(i, num_boards)

            base_map = copy.deepcopy(board)

            comb_map = self.generate_map(comb, base_map)

        

            locations = self.count_locations(comb_map)

            total_locations += locations

        #print "TOTAL", total_locations

        return total_locations


if __name__ == '__main__':


    input_0 = ["?.", ".O"]

    input_1 = ["???", 

               "?O?", 

               "???"]

    input_2 = ["...?.",

               "?....",

               ".O...",

               "..?..",

               "....?"] 

    input_3 = ["OOOOOOOOOOOOOOOOOOOOO"]

    input_4 = ["?????????OO??????????"]

    input_5 = ["OOO",

               "O?O",

               "OOO",

               "..."]


    xmark = XMarksTheSpot()

    

    start_time = time.time()

    result_0 = xmark.countArea(input_0)

    finish_time = time.time()

    time_0 = finish_time - start_time

    

    start_time = time.time()

    result_1 = xmark.countArea(input_1)

    finish_time = time.time()

    time_1 = finish_time - start_time


    start_time = time.time()

    result_2 = xmark.countArea(input_2)

    finish_time = time.time()

    time_2 = finish_time - start_time


    start_time = time.time()

    result_3 = xmark.countArea(input_3)

    finish_time = time.time()

    time_3 = finish_time - start_time


    start_time = time.time()

    result_4  = xmark.countArea(input_4)

    finish_time = time.time()

    time_4 = finish_time - start_time


    start_time = time.time()

    result_5 = xmark.countArea(input_5)

    finish_time = time.time()

    time_5 = finish_time - start_time


    print "RESULT 0 ", result_0, "Execution Time", time_0

    print "RESULT 1 ", result_1, "Execution Time", time_1

    print "RESULT 2 ", result_2, "Execution Time", time_2

    print "RESULT 3 ", result_3, "Execution Time", time_3

    print "RESULT 4 ", result_4, "Execution Time", time_4

    print "RESULT 5 ", result_5, "Execution Time", time_5
