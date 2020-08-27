import turtle


def main():
    star_onTurtle(200, 9, 8)
    turtle.exitonclick()


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


if __name__ == '__main__':
    main()
