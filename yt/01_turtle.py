import turtle as tt

tt.shape("turtle")
tt.penup()
tt.goto(0, 0)
tt.pendown()
tt.setheading(0)



def draw_shape(length: int, shapes_number: int):
    angle = 360 / shapes_number
    for i in range(shapes_number):
        tt.forward(length)
        tt.left(angle)

# SQUARE:
# draw_shape(100, 4)


# CIRCLE:
# draw_shape(1, 360)
# or:
# tt.circle(80)


# TEN_SQUARES:
def ten_squares(length: int):
    for i in range(10):
        draw_shape(length, 4)
        length += 10
        tt.penup()
        tt.backward(5)
        tt.right(90)
        tt.forward(5)
        tt.left(90)
        tt.pendown()

# ten_squares(10)


# SPIDER:

def spider(n: int):
    angle = 360 / n
    for i in range(n):
        tt.right(angle)
        tt.forward(100)
        tt.stamp()
        tt.penup()
        tt.backward(100)
        tt.pendown()

# spider(12)


# SPIRAL CIRCLE:

def spiral_circle(radius: int):
    for i in range(100):
        tt.circle(radius + i, 45)

# spiral_circle(10)


# SPIRAL SQUARE:

def spiral_square(size: int):
    for i in range(size * 4):
        tt.forward(i * 10)
        tt.right(90)

# spiral_square(10)


# REGULAR POLYGONS:

def regular_polygons(shapes: int):
    for i in range(10):
        tt.speed(1)
        size = shapes * 10
        draw_shape(size, shapes)
        tt.penup()
        tt.backward(size / 2)
        tt.right((360 / shapes) / 2)
        tt.forward(size / 2)
        tt.left((360 / shapes) / 2)
        tt.pendown()
        shapes += 1

# regular_polygons(3)


# FLOWER:

def flower(radius: int, petals: int):
    # tt.speed(0.1)
    angle = 360 / petals
    for i in range(petals):
        tt.circle(radius)
        tt.penup()
        tt.right(angle)
        tt.pendown()

# flower(50, 15)


# BUTTERFLY:

def butterfly(radius: int, wings: int):
    tt.penup()
    tt.right(90)
    tt.pendown()
    for i in range(wings):
        tt.circle(radius)
        tt.penup()
        tt.right(180)
        tt.pendown()
        tt.circle(radius)
        tt.penup()
        tt.right(180)
        tt.pendown()
        radius += radius / 2


# butterfly(10, 5)

def arch(radius, arches):
    tt.penup()
    tt.left(90)
    tt.pendown()
    for i in range(arches):
        tt.circle(radius * -1, 180)
        tt.circle((radius / 5) * -1, 180)

# arch(50, 5)


# SMILE:

def smile(size):
    tt.begin_fill()
    tt.color('yellow')
    tt.circle(size)
    tt.end_fill()
    tt.penup()
    tt.left(90)
    tt.forward(1.25 * size)
    tt.left(90)
    tt.forward(0.25 * size)
    tt.left(180)
    tt.pendown()
    tt.begin_fill()
    tt.color('blue')
    tt.circle(0.1 * size)
    tt.end_fill()
    tt.penup()
    tt.forward(0.5 * size)
    tt.pendown()
    tt.begin_fill()
    tt.circle(0.1 * size)
    tt.end_fill()
    tt.penup()
    tt.backward(0.25 * size)
    tt.right(90)
    tt.forward(0.25 * size)
    tt.pendown()
    tt.width(10)
    tt.color('black')
    tt.forward(0.25 * size)
    tt.penup()
    tt.right(90)
    tt.forward(0.5 * size)
    tt.left(90)
    tt.pendown()
    tt.color('red')
    tt.circle(0.5 * size, 180)
    tt.exitonclick()


# smile(150)


# STARS:

def stars(tops: int, size: int):
    if tops % 2 == 0:
        tops += 1
    angle = 180 / tops
    for i in range(tops):
        tt.forward(size)
        tt.right(180 - angle)

    tt.exitonclick()


# stars(4, 300)

