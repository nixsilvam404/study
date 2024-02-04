def input_seq() -> list:
    sequence = []
    while (inp := abs(int(input('input: ')))) != 0:
        sequence.append(inp)
    return sequence


def amount_num(lst : list) -> int:
    return len(lst)


def sum_num(lst: list) -> int:
    return sum(lst)


def prod_num(lst: list) -> int:
    prod = 1

    for i in lst:
        prod *= i

    return prod


def average(sumnum: int, quant: int ) -> int:
    return sumnum / quant


def biggest(lst: list) -> int:
    big = 1

    for i in lst:
        if i > big:
            big = i
    

    return lst.index(big) + 1


def oddnotodd(lst: list) -> int:
    odd = 0
    notodd = 0

    for i in lst:
        if i % 2 == 0:
            odd += 1
        else: 
            notodd += 1
    
    return odd, notodd


def second_big(lst: list) -> int:
    s_lst = list(set(lst))    
    return sorted(s_lst, reverse=True)[1]


def largest_amount(lst: list) -> int:
    count = 1
    big = 1

    for i in lst:
        if i > big:
            big = i
            count = 1
        elif i == big:
            count += 1

    return count
    


seq = input_seq()
amount = amount_num(seq)
summ = sum_num(seq)
odd_num, not_odd_num = oddnotodd(seq)

print(f'Amount of input numbers: {amount}')
print(f'Sum of input numbers: {summ}')
print(f'Product of input numbers: {prod_num(seq)}')
print(f'Average of input numbers: {average(summ, amount)}')
print(f'Serial number of biggest value: {biggest(seq)}')
print(f'Amount of odd numbers: {odd_num}\n \
      Amount of not odd numbers: {not_odd_num}')
print(f'Second largest number: {second_big(seq)}')
print(f'Quantity of largest numbers: {largest_amount(seq)}')
