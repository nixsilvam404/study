def calculations():
    x = list(input('Insert a float number with 2 digits after point: '))
    print(f'Fraction: {x[2] + x[3]}')
    print(f'First digit after decimal point: {x[2]}')


# calculations()


def calculations_2():
    x = float(input('Insert a float number with 2 digits after point: '))
    print(int(round(100*(x % 1))))
    print(int(x*10) % 10)


calculations_2()
