def sign(x: int):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


num = int(input('Input the number: '))
print(f'The octothorpe of number is {sign(num)}')


