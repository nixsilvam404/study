# It is required to determine whether a given year is a leap year. 
# (A year is considered a leap year if its number is divisible by 4 
#  but not divisible by 100, or if it is divisible by 400).

# Input Format

# An integer N is given as input - the year number (0 < N < 100000).

# Output Format

# Output True if the year is a leap year, and False otherwise.


def leap_year(num: int) -> bool:

    if num % 4 == 0 and num % 100 != 0 \
    or num % 400 == 0:
        return True
    else:
        return False
    

print(leap_year(1900))
print(leap_year(2000))