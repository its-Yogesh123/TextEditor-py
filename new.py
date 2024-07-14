# Python any version py3 recommended
# Modules Required :- Turtle only 
# You have to install turtle using command in terminal 
# "pip install turtle "  or "pip3 install turtle"
#  for mac users "brew install python-turtle"

# ----  If there any suggestion/correction regarding code then please contribute it to me on githuB.
import turtle as t

# Set up the screen
screen = t.Screen()
t.hideturtle()
screen.bgcolor("white")     # setting background
t.speed(1.5)     # for creating speed
t.up()
# ------ creating the skyblue rectangel initally for lower-body(legs)
t.goto(-101.0,3.0)
t.color("skyblue")
t.begin_fill()
t.goto(-101.0,-97.0)
t.goto(101.0,-97.0)
t.goto(101,3)
t.goto(-101,3)
t.end_fill()
t.color("black")
# ----function 
def click(x,y):
    print(x," ",y)
t.onscreenclick(click)
# ---- ellipse for foot
def ellipse(a,b):
    for _ in range(2):
        t.circle(a,90)
        t.circle(b,90)
# Function to draw a filled circle
def draw_circle(color, radius, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to draw Doraemon's face
# if not Subsribed my Channel plz Do it...
def draw_doraemon_face():
    # Draw face
    draw_circle("skyblue", 100, 0, 100)  # White face

    # Draw eyes
    draw_circle("#ffffff", 20, -20, 230)   # Left eye
    draw_circle("#ffffff", 20, 20, 230)    # Right eye
    draw_circle("#000000", 7, -15, 235)    # Left eyeball
    draw_circle("#000000", 7, 15, 235)     # Right eyeball

    # Draw nose
    draw_circle("#ff0000", 20, 0, 198)

    # Draw mouth
    t.penup()
    t.goto(-60, 210)
    t.pendown()
    t.setheading(-90)
    t.circle(60, 180)

# Function to draw Doraemon's body
def draw_doraemon_body():
    # Draw body
    draw_circle("skyblue", 120, 0, -50)  # Blue body

    # Draw belly
    draw_circle("#ffffff", 90, 0, -50)  # White bell
# Function to draw Doraemon's whiskers
def draw_doraemon_whiskers():
    # Draw whiskers
    t.pensize(2)
    t.penup()
    t.goto(30, 200)
    t.setheading(25)
    t.pendown()
    t.forward(40)

    t.penup()
    t.goto(-60, 213)
    t.setheading(335)
    t.pendown()
    t.forward(40)

    t.penup()
    t.goto(30, 187)
    t.setheading(0)
    t.pendown()
    t.forward(40)

    t.penup()
    t.goto(-65, 185)
    t.setheading(0)
    t.pendown()
    t.forward(40)
    # ---
    t.penup()
    t.goto(30, 175)
    t.setheading(-25)
    t.pendown()
    t.forward(40)

    t.penup()
    t.goto(-60, 157)
    t.setheading(25)
    t.pendown()
    t.forward(40)
def drawhands():
     draw_circle("skyblue", 30, -135, 20)  # Skyblue body
     draw_circle("skyblue", 30, 160, 20)  # SkyBlue body
# main function to Draw Doraemon 
def draw_doraemon():
    draw_doraemon_body()
    draw_doraemon_face()
    draw_doraemon_whiskers()
    drawhands()
    t.pensize(1.5)
    t.up()
    t.goto(0,199)
    t.down()
    t.goto(0,152)
    t.up()
    t.goto(-60,20)
    t.down()
    t.setheading(-90)
    t.circle(60,180)
    t.hideturtle()
    t.up()
    t.goto(-60,20)
    t.down()
    t.right(90)
    t.forward(120)
    # -- creating hands
    t.up()
    t.goto(-101,3)
    t.down()
    t.right(90)
    t.forward(100)
    # ----
    t.up()
    t.goto(0,-58)
    t.down()
    t.forward(42)
    # --
    t.up()
    t.goto(101,3)
    t.down()
    t.forward(100)
    # ---- foot making
    t.up()
    t.goto(-97,-95)
    t.right(45)
    t.down()
    ellipse(10,67)
    # ----
    t.up()
    t.goto(3,-95)
    t.down()
    ellipse(10,67)
    # ----
    t.done()
# Call the function to draw Doraemon
draw_doraemon()