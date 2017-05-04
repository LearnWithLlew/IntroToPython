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

