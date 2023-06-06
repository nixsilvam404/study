def numbers(num: int):
    next_num = num + 1
    prev_num = num - 1
    print(f'The next number for the number {num} is {next_num}')
    print(f'The previous number for the number {num} is {prev_num}')
    return next_num, prev_num


number = int(input('Please enter an integer number: '))
numbers(number)
