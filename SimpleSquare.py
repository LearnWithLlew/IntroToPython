import Colors
import Turtle
import MessageBox

Turtle.show()
Turtle.set_speed(10)
sides = MessageBox.ask_for_numerical_input("Hello")
for i in range(sides):
    Turtle.set_pen_color(Colors.get_random_color())
    Turtle.set_pen_width(i);
    Turtle.move(13)
    Turtle.turn(360.0 / sides)
    Turtle.show()

# Show the tortoise --#1
# Make the tortoise move as fast as possible --#6
# Do the following 4 times --#5.1
#       Change the color of the line the tortoise draws to "blue" --#4
#       Move the tortoise 50 pixels --#2
#       Turn the tortoise to the right (90 degrees) --#3
# Repeat --#5.2