import sys

import Colors
import Turtle

libDir = "/Users/llewellyn/PycharmProjects/LearnWithLlew/LearnWithLlew.jar"
sys.path.append(libDir)

from org.learnwithllew.courseware.recipes.quizzes.graders import SimpleSquareQuizGrader
from org.learnwithllew.courseware.recipes.quizzes.graders import SquareQuiz



class SimpleSquareQuiz(SquareQuiz):
    def question1(self):
        #Move the tortoise 110 pixels
        Turtle.move(110)
        pass

    def question2(self):
        #  Turn the tortoise 1/5 of 360 degrees to the right
        Turtle.turn(360/5)
        pass

    def question3(self):
         #  Change the color the tortoise draws to yellow
         Turtle.set_pen_color(Colors.Yellows.Yellow)

    def question4(self):
         #  //  Change the width of the line the tortoise draws to 5 pixels
        pass

if __name__ == '__main__':
    SimpleSquareQuizGrader().grade(SimpleSquareQuiz());
