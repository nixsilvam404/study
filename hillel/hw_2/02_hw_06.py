def presense(x):
    if abs(int(x)) in (range(10, 100, 10)):
        return True
    else:
        return False


number = float(input('Input the number: '))
print(presense(number))
