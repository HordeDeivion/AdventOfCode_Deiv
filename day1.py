

file_name_test="easy_input.txt"
file_name_challenge="input.txt"

def count_increases(fd):
    total_increases=0
    last_value = None
    for idx_row, row in enumerate(fd):
        if last_value:
            if last_value < int(row):
                total_increases+=1
        last_value= int(row)
    return total_increases

print("Starting counting")
tot = count_increases(open(file_name_challenge, "r"))
print("END counting")
print(str(tot))

