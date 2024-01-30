# The program receives a sequence of non-negative integers, 
# each number entered on a separate line. The sequence ends with 
# the number 0, upon reading which the program should end its work 
# and output the number of elements in the sequence (excluding the 
# terminating number 0). Numbers that follow the number 0 do not 
# need to be read.

# Input Format

# A sequence of integers is entered as input (each on a new line), 
# ending with the number 0. The number 0 is not included in the 
# sequence.

# Output Format

# Output the length of the sequence.


def make_list(inp: str) -> list:
    inp_list = [int(i) for i in inp.split("\n") if i != '']    
    return inp_list[:inp_list.index(0)]


def sequence_len(input_list: list) -> int:
    return len(input_list)


def make_input() -> str:
    some_inp = True
    inp_string = ''

    while some_inp:
        some_inp = input("input: ")
        inp_string += (some_inp + "\n")
        if not some_inp:
            break

    return inp_string


if __name__ == '__main__':
    print(sequence_len(make_list(make_input())))
