from turtle import Turtle, Screen
from prettytable import PrettyTable
oogway = Turtle()
oogway.shape("turtle")
oogway.color("DarkRed")
my_screen = Screen()
print(my_screen.canvheight)
table = PrettyTable()
oogway.speed(1)
oogway.forward(100)
my_screen.exitonclick()