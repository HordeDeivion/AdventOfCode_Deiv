
from functools import reduce
file_name_test="Day3_input_test.txt"
file_name_challenge="Day3_input_challenge.txt"



def line_toString_bit(line_toProcess):
    #Used in part One
    return sum(2**pos*value for pos,value in enumerate(line_toProcess))
     

def transform_data(list_zeros,list_ones):
    #Used in partOne
    final_ganmma= line_toString_bit([1 if x>y else 0 for x,y in zip(list_ones,list_zeros)])
    final_epsilon=line_toString_bit([1 if x<y else 0 for x,y in zip(list_ones,list_zeros)])
    
    print(f'Final ganma {final_ganmma}')
    print(f'Final epsilon {final_epsilon}')
    print(f'Final epsilon {final_ganmma*final_epsilon}')
    return -1

def get_number_bits(fd):
    #Part One
    line_lenght = None
    for line in fd:
        if not line_lenght:
            line_lenght=len(line)
            list_zeros=[0]*line_lenght
            list_ones =[0]*line_lenght
        line_bit = [int(x)  for x in line.strip()]
        for pos,bit in enumerate(line_bit[::-1]):
            if bit:
                list_ones[pos]+=1
            else:
                list_zeros[pos]+=1
            
    transform_data(list_zeros,list_ones)
    return 1

def get_bitCriteria(list_arrayBits,pos):
    # This function will return the most common/uncommon bit for a position 
    # that is specifid in pos
    # if most_common=true , gets the most_common bit
    bit_counter= 0
    for bit_array in list_arrayBits:
        if bit_array[pos]:
            bit_counter+=1
    
    # Return 1 if there are more 1
    return 1 if bit_counter>=((len(list_arrayBits)+1)//2) else 0

def get_filter_criteria(fd,max):
    #  if max = 1 
    #  take the most common

    all_lines = [ [int(x)  for x in line.strip()] for line in fd.readlines()]                
    line_lenght = len(all_lines[0]) 
    oxigen_value = []

    # Get oxigen Value
    for i in range(line_lenght):
        if len(all_lines)>1:
            mc_bit= get_bitCriteria(all_lines,i)                                             # Get most common bit
            if max:
                all_lines =list(filter(lambda arraybit: arraybit[i] == mc_bit, all_lines))    # Filter the new list
            else:
                mc_bit = 0 if mc_bit else 1
                all_lines =list(filter(lambda arraybit: arraybit[i] == mc_bit, all_lines)) 
            oxigen_value.append(mc_bit)
        else:
             oxigen_value.append(all_lines[0][i])

    print("I'm on get_filter_criteria")
    return oxigen_value



print("Starting program")


objetiveOxigen_bitarray = get_filter_criteria(open(file_name_challenge, "r"),True)
objetiveOxigen_value =line_toString_bit(objetiveOxigen_bitarray[::-1])

print(f'This is the result - BIT STRING - {objetiveOxigen_bitarray} - VALUE - {objetiveOxigen_value} ')
objetiveC02_bitarray= get_filter_criteria(open(file_name_challenge, "r"),False)
objetiveC02_value =line_toString_bit(objetiveC02_bitarray[::-1])

print(f'This is the result - BIT STRING - {objetiveC02_bitarray} - VALUE - {objetiveC02_value} ')

print(f'This is the result - multiplied {objetiveOxigen_value * objetiveC02_value} ')
print("END program")
