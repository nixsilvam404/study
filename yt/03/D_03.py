# Given a natural number N, print all the squares of natural numbers 
# that do not exceed N, in ascending order.

# IMPORTANT! This task requires the use of a loop.
# Input Format

# The program receives an integer N, not exceeding 10000, as input.
# Output Format

# The program should print a sequence of numbers in ascending order. 
# A space is used as a separator.


def squares_list(n: int) -> list:
    count = 1
    sq_list =[]

    while count ** 2 <= n:
        sq_list.append(count ** 2)
        count += 1
        
    return sq_list


print(squares_list(16))
print(squares_list(50))
print(squares_list(10000))