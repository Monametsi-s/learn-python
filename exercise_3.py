from turtle import Turtle, Screen
'''
#1 prints We like Python's turtles! 1000 times
for i in range(1000):
    print("We like Python's turtles!")

#2 Attriutes and methods of a phone
Attributes
-phone colour
-phone size
-phone weight

Methods
-Making a call
-Sending a text
-Taking poto



#3 Using a for loop to print
#One of the months of the year is ...
for i in ["Jan", "Feb", "March"]:
    print('One of the months of the year is '+ i)
#4
wn = Screen()
tess = Turtle()
tess.left(3645)

wn.mainloop()

#5 
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# loop that prints each of the numbers on a new line
for i in xs:
    print(i)
    print()

#loop that prints each number and its square on a new line.
for i,j in enumerate(map(lambda x: x**2, xs)):
    print(str(xs[i]) + " " + str(j))
    print()

#loop that adds all the numbers from the list
sum_total = 0
for i in xs:
    sum_total += i
print(str(sum_total))

# product of all the numbers in the list
product_total = 1
for i in xs:
    product_total *= i
print(str(product_total))


#7&8 A drunk pirate makes a random turn and then takes 100 
# stepsforward,makesanotherrandom turn, takes another 100 steps,
# turns another random amount,  A social science student records 
# the angle of each turn before the next 100 steps are taken. 
# Her experimental data is:

expermental_data = [160, -43, 270, -97, -43, 200, -940, 17, -86]
wn = Screen()
t = Turtle()
for i in expermental_data:
    t.forward(100)
    t.left(i)
#8  Enhance your program above to also tell us what 
#   the drunk pirate’s heading is after he has finished stumbling around
t_new = Turtle()
t_new.color("red")
t_new.left(180)
t_new.forward(22)
t_new.left(63)
t_new.forward(90)
t_new.left(-86)

wn.mainloop()

#9 You would need an angle of 360/18 = 20 degrees

#11 Write a program to write a star
wn = Screen()
star = Turtle()
angle = -(180-36)

star.penup()            # Centrering the star
star.backward(100)
star.left(90)
star.forward(50)
star.right(90)
star.pendown()
star.pensize(3)        # Making the star thick

for i in range(5):     #Creating the star
    star.forward(200)
    star.left(angle)
star.hideturtle()

wn.mainloop()
'''
#12 Drawing face of the clock

def clock_face():

    wn = Screen()
    wn.bgcolor("lightgreen")
    
    totti = Turtle()
    totti.color("blue")
    totti.shape("turtle")
    totti.pensize(2)
    totti.penup()
    for i in range(12):
        totti.forward(100)
        totti.pendown()
        totti.forward(15)
        totti.penup()
        totti.forward(15)
        totti.stamp()
        totti.backward(130)
        totti.left(30)
    wn.mainloop() 

# 13 When you ask for its type, what do you get?
turtle_1 = Turtle()
print(type(turtle_1)) #Output <class 'turtle.Turtle'>


#14 Collective noun for turtles
# - Bale 
