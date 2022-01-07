#สร้างการ GUI ควบคุมผ่าน keybroad

from turtle import Turtle, Screen

timmy = Turtle()
timmy.speed("fastest")
screen = Screen()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.back(10)

def counter_clockwise():
    timmy.left(10)

def clockwise():
    timmy.right(10)

def clear():
    timmy.penup()
    timmy.clear()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()