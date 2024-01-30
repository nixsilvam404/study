# Given a natural number N, output the smallest integer k such that 
# 2^k >= N.

# IMPORTANT! This task requires the use of a loop. The use of the 
# 'if' statement is prohibited. In this task, you cannot use 
# exponentiation.

# Input Format

# The program receives a natural number N as input, not 
# exceeding 10000.

# Output Format

# You need to print the smallest k that meets the condition 
# of the task.


def binary_logarithm(n: int) -> int:
    k = 0
    result = 1

    while result < n:
        result *= 2
        k += 1

    return k

print(binary_logarithm(1000))
print(binary_logarithm(16))