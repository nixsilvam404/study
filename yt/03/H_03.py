# Count the number of even elements in an array of integers that ends 
# with a zero. The zero itself should not be counted.

# Input Format

# An array of numbers ending with zero (each number on a new line, zero 
# is not part of the array)

# Output Format

# A single number — the result.


from F_03 import make_list

def even_number(s: list) -> int:
    count = 0

    for i in s:
        if int(i) % 2 == 0 and int(i) != 0:
            count += 1

    return count


def input_before_zero():
    some_inp = True
    inp_string = ''

    while some_inp:
        some_inp = input("input: ")
        inp_string += (some_inp + "\n")
        if some_inp == '0':
            break

    return inp_string

if __name__ == '__main__':
    print(even_number(make_list(input_before_zero())))