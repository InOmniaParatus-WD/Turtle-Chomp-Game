# Turtle Graphics Game – Space Turtle Chomp
import turtle
import math
import random
import winsound
import time

# Set up screen
turtle.setup(680,680)
screen = turtle.Screen()
screen.bgcolor('black')
screen.bgpic('images/kbgame-bg.gif')
screen.tracer(3)

# Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
mypen.color('gray')

for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.shapesize(2)
player.color('mediumaquamarine')
player.shape('turtle')
player.penup()
player.speed(0)

# Create opponent turtle
comp = turtle.Turtle()
comp.color('red')
comp.shape('turtle')
comp.penup()
comp.shapesize(2)
comp.setposition(random.randint(-290, 290), random.randint(-290, 290))
comp.speed(0)

# Create competition score
mypen2 = turtle.Turtle()
mypen2.color('red')
mypen2.hideturtle()

# Create variable score
score = 0
comp_score = 0

# Create food
maxFoods = 10
foods = []

for count in range(maxFoods):
    new_food = turtle.Turtle()
    new_food.shapesize(1)
    new_food.color("green")
    new_food.shape("circle")
    new_food.penup()
    new_food.speed(0)
    new_food.setposition(random.randint(-290, 290), random.randint(-290, 290))
    foods.append(new_food)

# Set speed variable
speed = 1

# Set game time limit for 1 minute (60 seconds)
timeout = time.time() + 10*6

# Define functions
def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def increase_speed():
    global speed
    if speed < 8:
        speed += 0.5
    
def decrease_speed(): 
    global speed
    if speed != 1: 
        speed -= 0.5

# Check turtle's collision with cabbage
def isCollision(t1, t2):
       d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
       if d < 20:
           return True
       else:
           return False

# Set keyboard binding
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')
turtle.onkey(decrease_speed, 'Down')

while True:
    gametime = 0
    if gametime == 6 or time.time() > timeout:
        break
    gametime = gametime - 1

    player.forward(speed)
    comp.forward(12)
    # Boundary Comp Checking x coordinate
    if comp.xcor() > 290 or comp.xcor() < -290:
        comp.right(180)

    # Boundary Comp Checking y coordinate
    if comp.ycor() > 290 or comp.ycor() < -290:
        comp.right(180)

    #Boundary Checking x cordinate
    if player.xcor() > 290 or player.xcor() <-290:
        player.right(180)
        winsound.PlaySound('sounds/bounce.wav', winsound.SND_ASYNC)
    #Boundary Checking x coordinate
    if player.ycor() > 290 or player.ycor() <-290:
        player.right(180)
        winsound.PlaySound('sounds/bounce.wav', winsound.SND_ASYNC)

    #Move Food around
    for food in foods:
        food.forward(3)

        #Boundary Food Checking x coordinate
        if food.xcor() > 290 or food.xcor() <-290:
            food.right(180)
            winsound.PlaySound('sounds/bounce.wav', winsound.SND_ASYNC)

        #Boundary Food Checking y coordinate
        if food.ycor() > 290 or food.ycor() <-290:
            food.right(180)
            winsound.PlaySound('sounds/bounce.wav', winsound.SND_ASYNC)

        #Collision checking
        if isCollision(player, food):
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0,360))
            winsound.PlaySound('sounds/chomp.wav', winsound.SND_ASYNC)

            score += 1
            
            # Draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring ="Score: %s" % score
            mypen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

            # Comp Collision checking
        if isCollision(comp, food):
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0,360))
            winsound.PlaySound('sounds/chomp.wav', winsound.SND_ASYNC)
            comp_score += 1
            # Draw the Comp score on the screen
            mypen2.undo()
            mypen2.penup()
            mypen2.hideturtle()
            mypen2.setposition(200, 305)
            scorestring ="Score: %s" % comp_score
            mypen2.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

# Comparing players' scores
if (int(score) > int(comp_score)):
    mypen.setposition(0, 0)
    mypen.color("yellow")
    mypen.write("Game Over: You WIN", False, align="center", font=("Arial", 28, "normal"))
else:
    mypen.setposition(0, 0)
    mypen.color("yellow")
    mypen.write("Game Over: You LOSE", False, align="center", font=("Arial", 28, "normal"))

delay = input("Press Enter to finish.")

# Further study: Add function to restart the game