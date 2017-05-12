import sys

import Colors
import Turtle

libDir = "LearnWithLlew.jar"
sys.path.append(libDir)

from org.learnwithllew.courseware.recipes.quizzes.graders import SimpleSquareQuizGrader
from org.learnwithllew.courseware.recipes.quizzes.graders import SquareQuiz



class SimpleSquareQuiz(SquareQuiz):
    def question1(self):
        #Move the tortoise 110 pixels
        pass

    def question2(self):
        #  Turn the tortoise 1/5 of 360 degrees to the right
        pass

    def question3(self):
        #  Change the color the tortoise draws to yellow
        pass

    def question4(self):
         #  //  Change the width of the line the tortoise draws to 5 pixels
        pass

if __name__ == '__main__':
    SimpleSquareQuizGrader().grade(SimpleSquareQuiz());
