# The sequence consists of natural numbers and ends with the number 0. 
# A total of no more than 10,000 numbers are entered (excluding the 
# terminating number 0). Determine how many elements of this sequence 
# are equal to its largest element. Numbers that follow the number 0 do 
# not need to be read.

# Input Format

# A sequence of integers is entered, ending with the number 0 (the number 
# 0 itself is not part of the sequence).

# Output Format

# Print the answer to the task (a single number).


from F_03 import make_list


def quantity_of_largest_element(s: list) -> int:
    quantity = 1
    largest_element = 0
    for i in s:
        if i > largest_element:
            largest_element = i
        elif i == largest_element:
            quantity += 1
    return quantity


string = '1\n3\n3\n1\n0'
print(quantity_of_largest_element(make_list(string)))
