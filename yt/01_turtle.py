import turtle as tt

tt.shape("turtle")


def draw_shape(length, shapes_number):
    angle = 360 / shapes_number
    for i in range(0, shapes_number):
        tt.forward(length)
        tt.left(angle)


# SQUARE:
# draw_shape(100, 4)

# CIRCLE:
# draw_shape(1, 360)
# or:
# tt.circle(80)

# TEN_SQUARES:
def ten_squares(length):
    for i in range(0, 10):
        draw_shape(length, 4)
        length = length + 10
        tt.penup()
        tt.backward(length / 2)
        tt.right(90)
        tt.forward(length / 2)
        tt.left(90)
        tt.pendown()


# ten_squares(10)

# SPIDER:

def spider(n):
    angle = 360 / n
    for i in range(0, n):
        tt.right(angle)
        tt.forward(100)
        tt.stamp()
        tt.penup()
        tt.backward(100)
        tt.pendown()


# spider(12)

# SPIRAL CIRCLE:

def spiral_circle(radius):
    for i in range(100):
        tt.circle(radius + i, 45)


# spiral_circle(10)


# SPIRAL SQUARE:

def spiral_square(size):
    for i in range(size * 4):
        tt.forward(i * 10)
        tt.right(90)


# spiral_square(10)

# REGULAR POLYGONS:


