# Turtle Graphics Game – Space Turtle Chomp
import turtle

# Set up screen
turtle.setup(650,650)
windowScreen = turtle.Screen()
windowScreen.bgcolor('paleturquoise')

# Create player turtle
player = turtle.Turtle()
player.color('darkgreen')
player.shape('turtle')
player.penup()

# Set speed variable
speed = 1

# Move the turtle
while True:
    player.forward(speed)

 