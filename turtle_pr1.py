import turtle
import multitasking
colors = ['green', 'orange', 'purple', 'red', 'yellow', 'blue', 'white', 'pink', 'brown']

screen = turtle.Screen()
screen.bgcolor('black')

@multitasking.task
def print_figure(vertex, speed_val, pos=(0,0), max_size=250):
    col = 0
    pen = turtle.Turtle()
    pen.setpos(pos)
    pen.speed(speed_val)

    ang = (360//vertex)-1

    for i in range(max_size):
        pen.pencolor(colors[col])
        pen.width(i//100 + 1)
        pen.forward(i)
        pen.left(ang)
        col = (col or 9) -1

print_figure(3, 0, (-300,200), 100)
print_figure(4, 0, (0,200), 100)
print_figure(5, 0, (300,200), 100)
print_figure(6, 0, (-300,-200), 100)
print_figure(7, 0, (0,-200), 100)
print_figure(8, 0, (300,-200), 100)

screen.exitonclick()
