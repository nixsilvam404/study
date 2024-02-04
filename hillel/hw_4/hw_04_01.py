def quantity_of_days(x: int, y: int) -> int:
    count = 1

    while x <= y:
        x *= 1.1
        count += 1

    return count

km1 = int(input('В первый день спортсмен пробежал (км):'))
km2 = int(input('Пробег спортсмена (км):'))

print(f'Номер дня, на который пробег спортсмена составит не менее {km2} км: {quantity_of_days(km1, km2)}')

