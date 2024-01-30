# Determine the sum of all elements of the sequence that ends 
# with the number 0.
# Numbers following zero do not need to be read.

# Input Format

# Elements of the sequence are input one by one, each as an 
# integer on a new line. Numbers are entered until 0 is input.

# Output Format

# Output a single integer - the sum of the sequence.


from F_03 import make_input
from F_03 import make_list


def sequence_sum(seq_list: list) -> int:
    list_sum = 0

    for i in seq_list:
        list_sum += i

    return list_sum


if __name__ == '__main__':
    print(sequence_sum(make_list(make_input())))