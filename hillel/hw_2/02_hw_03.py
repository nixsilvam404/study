def vasya(v: int, t: int):
    if v > 0:
        point = v * t
    else:
        point = 100 + (v * t)
    return point


speed = int(input('''Enter the Vasya's speed (km/h):'''))
time = int(input('''Enter the time of Vasya's rally (in hours):'''))
print(vasya(speed, time))
