# The sequence consists of natural numbers and ends with the number 0. 
# Determine the value of the largest element in the sequence.

# Numbers following zero do not need to be read.

# Input Format

# A sequence of integers is entered, ending with the number 0 
# (the number 0 itself is not part of the sequence).

# Output Format

# Print the answer to the task (a single number).


from F_03 import make_list


def largest_element(s):
    big_element = 0

    for i in s:
        if i > big_element:
            big_element = i

    return big_element


if __name__ == '__main__':
    sequence = "1\n7\n9\n0"
    print(largest_element(make_list(sequence)))