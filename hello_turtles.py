import turtle            # Allows us to use turtle
wn = turtle.Screen()     # Creates a playground for turtles 
wn.bgcolor("lightgreen") # Set the window background color 
wn.title("Tess and Alex") # Set the window title
'''
tess = turtle.Turtle()   # Create a turtle, asssign it to Tess
tess.color("red")        #Set some attributes for Tess 
tess.pensize(5)
alex = turtle.Turtle()  # Create a turtle, assign to alex

test = turtle.Turtle()
test.color("blue")
test.pensize(4)
alex.forward(100)        # Make Alex draw a rectangle
alex.left(90)           
alex.forward(100)       
alex.left(90)           
alex.forward(100)       
alex.left(90)           
alex.forward(100)       
alex.left(90)

tess.forward(100)       #Make tess draw an euilateral triangle
tess.left(120)
tess.forward(100)
tess.left(120)
tess.forward(100)
tess.right(60)         #Make tesss and move backwards by 100 units
tess.forward(100)

test.forward(75)
test.left(72)
test.forward(75)
test.left(72)
test.forward(75)
test.left(72)
test.forward(75)
test.left(72)
test.forward(75)
test.left(72)
'''
def draw_shape(sides, length):
    my_shape = turtle.Turtle()
    #my_shape.speed(5)
    #my_shape.penup()
    turn = 360 / sides
    for i in range(sides):
        my_shape.forward(length)
        my_shape.left(turn)
        #my_shape.stamp()
    return

draw_shape(3,200)

wn.mainloop()           # Wait for user to close window
