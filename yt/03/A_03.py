# There is a three-digit number. Need to find a sum of these digits.

def three_digit_sum (num: int) -> int:

    num_list = [int(i) for i in str(num)] #Create a list of number from int
    digit_sum = 0

    for i in num_list:
        digit_sum += i

    return digit_sum


print(three_digit_sum(179))