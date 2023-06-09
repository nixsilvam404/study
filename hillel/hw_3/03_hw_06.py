def knights_move():
    x1 = int(input('Input the first horizontal coordinates: '))
    y1 = int(input('Input the first vertical coordinates: '))
    x2 = int(input('Input the second horizontal coordinates: '))
    y2 = int(input('Input the first vertical coordinates: '))
    diff_x = abs(x1 - x2)
    diff_y = abs(y1 - y2)
    if diff_x == 1 and diff_y == 2 or diff_x == 2 and diff_y == 1:
        print('The knight\'s move is possible.')
    else:
        print('The knight\'s move is impossible')


knights_move()




