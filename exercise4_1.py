import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

t = turtle.Turtle()
t.color("red")
t.pencolor("blue")
t.speed(0)
#t.penup()
#t.goto(-wn.window_width() / 2, 0)
#t.pendown()
def draw_mysquare(size):
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.penup()
    t.forward(40)
    t.pendown()
def draw_square(i):
    for _ in range(4):
        t.forward(i)  # Move the Turtle forward by 100 units
        t.left(90)      # Turn the Turtle right by 90 degrees
def draw_spiral():
    t.clear()
    t.penup()
    t.goto(-15,-15)
    t.pendown()
    i = 5
    while i < 300:
        t.right(90)
        t.forward(i)
        i += 3
    t.right(90)

def draw_spiral_1():
    """A spiral keeps changing angle with turn"""
    t.clear()
    t.penup()
    t.goto(-15,-15)
    t.pendown()
    i = 5
    j = 90
    while i < 300:
        for a in range(4):
            t.right(j)
            t.forward(i)
            i += 2
        j -= 0.1
    
    t.right(90)


def incremental_square():
    t.goto(-20, -20)
    for i in [20, 40, 60, 80, 300]:
        draw_square(i)
        t.penup()
        t.goto((int(t.xcor())-10), (int(t.ycor()) -10))
        t.pendown()
        




for i in [1, 2, 3, 4, 5]:
    draw_mysquare(20)

t.clear()
incremental_square()
draw_spiral()
draw_spiral_1()


wn.mainloop()