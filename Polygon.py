import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

my_screen.bgcolor('gray')
my_screen.title('ReGaLToS')

my_turtle.color('blue')

def parallelogram():
    for i in range(2):
        my_turtle.forward(100)
        my_turtle.left(80)
        my_turtle.forward(50)
        my_turtle.left(100)

parallelogram()
