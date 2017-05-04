import sys

libDir = "/Users/llewellyn/PycharmProjects/LearnWithLlew/LearnWithLlew.jar"
sys.path.append(libDir)

from org.learnwithllew.teachingextensions.logo import Colors


def get_random_color():
    return Colors.getRandomColor()

class Reds(object):
    Red = Colors.Reds.Red
class Blues(object):
    Blue = Colors.Blues.Blue