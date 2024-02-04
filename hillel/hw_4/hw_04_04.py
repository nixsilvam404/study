def stairs(n: int):
    if n > 0 and n < 10:
        prnt = ''
        for i in range(1, n+1):
            prnt += str(i)
            print(prnt) 
    else: 
        raise SyntaxError('n must be > 0 and < 10')

stairs(2)
