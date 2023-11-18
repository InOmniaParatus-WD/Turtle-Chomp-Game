# Turtle Graphics Game – Space Turtle Chomp
import turtle

# Set up screen
turtle.setup(650,650)
screensize = turtle.Screen()
screensize.bgcolor('paleturquoise')

# Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
mypen.color('white')

for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color('darkgreen')
player.shape('turtle')
player.penup()
player.speed(0)

# Set speed variable
speed = 1

# Define functions
def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def increase_speed():
    global speed
    if speed < 5:
        speed += 0.5
    #     print(speed)
    # else:
    #     print(speed)
    #     print("Can't go any  faster!!!")
    
def decrease_speed(): 
    global speed
    if speed != 1: 
        speed -= 0.5
    #     print(speed)
    # if speed == 0:
    #     print("I can't walk anymore...")

# Set keyboard binding
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')
turtle.onkey(decrease_speed, 'Down')

# Move the turtle
while True:
    player.forward(speed)

    # Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)

    # Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)