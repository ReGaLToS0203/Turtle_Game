import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

my_screen.bgcolor('gray')
my_screen.title('ReGaLToS')

my_turtle.color('blue')

def sqrfunc(size):
    for i in range(4):
        my_turtle.fd(size)
        my_turtle.left(90)
        size = size + 5

sqrfunc(10)
sqrfunc(20)
sqrfunc(30)
sqrfunc(40)
sqrfunc(50)
sqrfunc(60)
sqrfunc(70)
sqrfunc(80)
sqrfunc(90)
sqrfunc(100)
sqrfunc(110)
sqrfunc(120)
sqrfunc(130)
