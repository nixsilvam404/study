def ab (a: int, b: int) -> list:
    ab_list = []

    if a < b:
        while a <= b:
            ab_list.append(a)
            a += 1

    elif a > b:
        while a >= b:
            ab_list.append(a)
            a -= 1
            
    return ab_list

print(ab(2,15))
print(ab(20,5))