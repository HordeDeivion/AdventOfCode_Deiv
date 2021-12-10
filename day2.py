

submarinePosition= [0,0]     #Determinates X,Y position


file_name_test="Day2_input_test.txt"
file_name_challenge="Day2_input_challenge.txt"

def get_submarine_position(fd):


    for idx_row, row in enumerate(fd):
        test_divided = row.split()
        if test_divided[0]== "forward":
            submarinePosition[0] += int(test_divided[1])
        if test_divided[0]== "down":
            submarinePosition[1] += int(test_divided[1])
        if test_divided[0]== "up":
            submarinePosition[1] -= int(test_divided[1])

print("Starting counting")
get_submarine_position(open(file_name_challenge, "r"))
print("END counting")
print(str(submarinePosition))