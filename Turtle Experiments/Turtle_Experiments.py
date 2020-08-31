import turtle
import random


def main():
    star_onTurtle(100)
    turtle.exitonclick()


def draw_yin_yang(radius=200):
    # outer circle
    draw_fill_circle(radius)

    # black semi-circle / lower end / white semi-circle
    draw_fill_circle(radius / 2, 180, 0, radius, 90, 'black', 'black')
    draw_fill_circle(radius, 180, -radius, radius, -90, 'black', 'black')
    draw_fill_circle(radius / 2, 180, 0, radius, -90, 'black', 'white')

    # small circles
    draw_fill_circle(radius / 10, 360, - radius / 2 + radius / 10, radius, 90, 'white', 'white')
    draw_fill_circle(radius / 10, 360, radius / 2 + radius / 10, radius, 90, 'black', 'black')

    turtle.hideturtle()


def draw_fill_circle(radius, extend=360, x_start=turtle.xcor(), y_start=turtle.ycor(), heading=turtle.heading(),
                     line_color="black", fill_color='white'):
    turtle.penup()
    turtle.color(line_color, fill_color)
    turtle.setposition(x_start, y_start)
    turtle.setheading(heading)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius, extend)
    turtle.end_fill()


def draw_radioactive(size=300):
    # draw background
    turtle.begin_fill()
    turtle.color('black', 'yellow')
    for j in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()

    # draw arcs
    turtle.color('black')
    angle = 0
    for i in range(3):
        # line
        turtle.penup()
        turtle.setheading(angle)
        turtle.setposition(size / 2, size / 2)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward((size / 2) * 0.8)

        # arc circle
        turtle.setheading(angle + 90)
        turtle.circle((size / 2) * 0.8, 60)

        turtle.end_fill()
        angle += 120

    # draw middle circle
    turtle.penup()
    turtle.color('yellow', 'black')
    turtle.setposition(size / 2, size / 2 - size / 10)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size / 10)
    turtle.end_fill()
    turtle.hideturtle()


def draw_olympic_symbol(size=30):
    space = 0.3
    lst = [['blue', 0, 0],
           ['black', size * (1 + space), 0],
           ['red', 2 * size * (1 + space), 0],
           ['yellow', 0.5 * size * (1 + space), -size / 2],
           ['green', 1.5 * size * (1 + space), -size / 2]]
    turtle.pensize(4)
    turtle.hideturtle()
    for el in lst:
        turtle.color(el[0])
        turtle.penup()
        turtle.setposition((el[1], el[2]))
        turtle.pendown()
        turtle.circle(size / 2)


def draw_squares_rot(size_ini=50, nr=5):
    # Draw concentric squares
    # 2.14
    incr = (size_ini * 1.2) / nr
    angle = 40
    angle_incr = 180 / nr
    turtle.hideturtle()
    for i in range(nr):
        turtle.setheading(angle + i * angle_incr)
        for j in range(4):
            turtle.forward(size_ini)
            turtle.right(90)
        size_ini += incr


def draw_squares(size_ini=50, nr=5):
    # Draw concentric squares
    # 2.14
    incr = size_ini / nr
    turtle.hideturtle()
    for i in range(nr):
        turtle.penup()
        turtle.setposition(-(incr * i) / 2, (incr * i) / 2)
        turtle.pendown()
        for j in range(4):
            turtle.forward(size_ini)
            turtle.right(90)
        size_ini += incr


def draw_walls(size):
    turtle.begin_fill()
    turtle.color('black', 'green')
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()


def draw_chimney(size):
    turtle.begin_fill()
    turtle.color('black')
    turtle.setposition((size * 0.6, 0))
    for i in range(2):
        turtle.forward(size * 0.2)
        turtle.left(90)
        turtle.forward(size * 0.8)
        turtle.left(90)
    turtle.end_fill()


def draw_roof(size):
    turtle.penup()
    turtle.setposition((0, 0))
    turtle.begin_fill()
    turtle.color('black', 'red')
    turtle.pendown()
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()


def draw_home(size=50):
    turtle.hideturtle()
    draw_walls(size)
    draw_chimney(size)
    draw_roof(size)


def draw_hexagon(size=50):
    # 2.11
    turtle.hideturtle()
    for i in range(6):
        turtle.setheading(60 * i)
        turtle.forward(size)
        turtle.right(120)
        turtle.forward(size)
        turtle.right(120)
        turtle.forward(size)


def elliptical_stamp():
    turtle.shape('circle')
    turtle.shapesize(0.3, 0.3)
    for i in range(360):
        turtle.up()
        turtle.forward(1 + i / 150)
        turtle.right(2)
        if i % 20 == 0:
            turtle.stamp()


def draw_clock():
    t1 = turtle.Turtle()
    angle = 360 / 12
    t1.setheading(90)
    t1.hideturtle()
    for i in range(12):
        t1.up()
        t1.right(angle)
        t1.setposition((0, 0))
        t1.forward(80)
        t1.pd()
        t1.forward(20)
        t1.pu()
        t1.forward(15)
        t1.write(i + 1, font=('Arial', 10, 'bold'))


def draw_smile(size):
    # size - face radius

    # Draw face
    turtle.penup()
    turtle.setpos(0, -size)
    turtle.pendown()
    turtle.circle(size)

    # Draw eyes
    draw_eyes(size)

    # draw mouth
    turtle.penup()
    turtle.setpos(0, -0.6 * size)
    turtle.pendown()
    turtle.circle(size * 2, -20)
    turtle.penup()
    turtle.setpos(0, -0.6 * size)
    turtle.setheading(0)
    turtle.pendown()
    turtle.circle(size * 2, 20)

    turtle.hideturtle()
    turtle.exitonclick()


def draw_eyes(size):
    turtle.penup()
    turtle.setpos(-size / 3, size * 0.3)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(size / 5)
    turtle.penup()
    turtle.setpos(size / 3, size * 0.3)
    turtle.pendown()
    turtle.circle(size / 5)
    turtle.end_fill()


def shape_a_turtle():
    turtle.penup()
    turtle.begin_poly()
    star_onTurtle(5)
    turtle.end_poly()
    turtle.pendown()
    star = turtle.get_poly()
    turtle.register_shape('star', star)


def random_walk_onTurtle():
    for i in range(random.randint(0, 20)):
        turtle.right(random.randrange(0, 360))
        turtle.forward(random.randrange(0, 200))


def star_onTurtle(size=100, number_edges=5, repeat=1):
    angle = 360 / number_edges
    if repeat == 1:
        size_change = 0
    else:
        size_change = size / repeat / number_edges

    for j in range(repeat):
        for i in range(number_edges):
            turtle.hideturtle()
            turtle.forward(size)
            turtle.right(angle * 2)
            size -= size_change


def salta_tartaruga(tarta, distancia):
    tarta.penup()
    tarta.forward(distancia)
    tarta.pendown()


def poligno_regular(comp_lados, num_lados):
    '''
    Desenha um polígno regular
    :return:
    '''
    for i in range(num_lados):
        turtle.hideturtle()
        turtle.forward(comp_lados)
        turtle.right(360 / num_lados)


if __name__ == '__main__':
    main()
