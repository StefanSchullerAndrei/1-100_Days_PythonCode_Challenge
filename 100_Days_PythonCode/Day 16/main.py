# import another_module
# print(another_module.another_module)
#
# from turtle import Turtle, Screen
#
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cadetblue3")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#
import prettytable
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
print(table)
