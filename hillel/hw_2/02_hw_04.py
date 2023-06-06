def leap_year(number: int):
    if number > 0:
        if number % 4 == 0 and number % 100 != 0 or number % 400 == 0:
            return True
        else:
            return False
    else:
        print('The number must be > 0')


year = int(input('Please input the year: '))
if leap_year(year):
    print('YES')
else:
    print('NO')
