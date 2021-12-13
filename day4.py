


import numpy as np
from functools import reduce

file_name_test="Day4_input_test.txt"
file_name_challenge="Day4_input_challenge.txt"


objetive_numbers = []               # List of numbers to check
list_bingo_cards = []               # List of bingo cards   
list_checked_values = []            # Matrix Array with 1s to check values in line

boardDIM = 5                        # Set board dimension

def check_row(index,i):
    global list_checked_values
    for j in range(boardDIM):
        if list_checked_values[index][i][j]:
            return 0
    return 1

    
def check_column(index,j):
    global list_checked_values

    for i in range(boardDIM):
        if list_checked_values[index][i][j]:
            return 0
    return 1

def calculate_result(index,number):
    global list_checked_values
    global list_bingo_cards

    total_sum = 0
    
    for i in range(boardDIM):
        for j in range(boardDIM):
            if list_checked_values[index][i][j]:
                total_sum+=list_bingo_cards[index][i][j]
    return total_sum*number      

def go_bingo():
    global list_checked_values
    global list_bingo_cards

    for number in objetive_numbers:

        for index,card in enumerate(list_bingo_cards):
            for i in range(boardDIM):
                for j in range(boardDIM):
                    if card[i][j] == number:
                        list_checked_values[index][i][j] = 0
                        if(check_row(index,i)):
                            return index,number
                        if(check_column(index,j)):
                            return index,number
    return -1,-1

def read_file(fd):
    global objetive_numbers
    global list_bingo_cards
    global list_checked_values

    counter = 0
    list_numbers = []
    

    # Read header 
    objetive_numbers = [int(x) for x in fd.readline().split(',')]
    fd.readline()
    # Process the rest of the document
    for line in fd.readlines():
        if counter == boardDIM:
            list_bingo_cards.append(np.array(list_numbers,dtype=int))
            list_checked_values.append(np.ones((boardDIM,boardDIM),dtype=int))
            list_numbers=[]
            counter=0
        elif counter < boardDIM:
            list_numbers.append([int(x) for x in line.strip().split()])
            counter+=1
    list_bingo_cards.append(np.array(list_numbers))
    list_checked_values.append(np.ones((boardDIM,boardDIM),dtype=int))

    return list_bingo_cards        


print("Hello world")

print(read_file(open(file_name_challenge, "r")))
index,number = go_bingo()
print(f'\n\n COINCIDENCE MATRIX \n\n {list_checked_values}')
print(f'\n\n Line Matching \n\n {calculate_result(index,number)}')

print("End world")