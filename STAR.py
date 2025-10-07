import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

my_screen.bgcolor('gray')
my_screen.title('ReGaLToS')

my_turtle.color('blue')

def star():
    my_turtle.right(75)
    my_turtle.forward(100)

    for i in range(4):
        my_turtle.right(144)
        my_turtle.forward(100)

def tilted_star():
    my_turtle.left(75)
    my_turtle.forward(100)

    for i in range(4):
        my_turtle.left(144)
        my_turtle.forward(100)
star()

tilted_star()

my_turtle.left(90)
tilted_star()

my_turtle.left(90)
tilted_star()
my_turtle.left(90)
tilted_star()
my_turtle.left(90)
tilted_star()
my_turtle.left(90)
tilted_star()
my_turtle.left(90)
tilted_star()
my_turtle.left(90)
tilted_star()
my_turtle.left(90)
tilted_star()
my_turtle.left(90)
tilted_star()
my_turtle.left(90)
tilted_star()
my_turtle.left(90)
tilted_star()
my_turtle.left(90)
tilted_star()
my_turtle.left(90)
tilted_star()
my_turtle.left(90)
tilted_star()
my_turtle.left(90)
tilted_star()
my_turtle.left(90)
tilted_star()
