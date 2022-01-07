#ส้ร้างเกม แข่งเต่าจาก GUI

from turtle import Turtle, Screen, color
import random

timmy = Turtle(shape="turtle")
tom = Turtle(shape="turtle")
jame = Turtle(shape="turtle")
tony = Turtle(shape="turtle")
arm = Turtle(shape="turtle")
ter = Turtle(shape="turtle")

turtle_player = [timmy, tom, jame, tony, arm, ter]
screen = Screen()
screen.setup(width=500, height=400)
choose_turtle = screen.textinput(title="Make your bet", prompt="We have six color turtles including 'red', 'orange', 'yellow', 'green', 'blue', 'purple' \nwhich turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(6):
    position_y = i * 33.3
    turtle_player[i].color(colors[i])
    turtle_player[i].penup()
    turtle_player[i].goto(x=-230, y=-100 + position_y)

again = True
while again:
    for i in range(6):
        walk = random.randint(0, 10)
        turtle_player[i].forward(walk)
        if turtle_player[i].xcor() > 230:
            again = False
            winner = colors[i]
            if winner == choose_turtle:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
        else:
            pass



screen.exitonclick()
