import turtle

my_turtle = turtle.Turtle()

def square(x,y):
           my_turtle.forward(x)
           my_turtle.right(y)
           my_turtle.forward(x)
           my_turtle.right(y)
           my_turtle.forward(x)
           my_turtle.right(y)
           my_turtle.forward(x)
           my_turtle.right(y)
           my_turtle.forward(x)
           my_turtle.right(y)
           my_turtle.forward(x)
           my_turtle.right(y)
           my_turtle.forward(x)
           my_turtle.right(y)
           my_turtle.forward(x)
           my_turtle.right(y)
           my_turtle.forward(x)
           
for i in range(6):
        square(50,360)
