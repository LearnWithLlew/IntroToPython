import sys

libDir = "/Users/llewellyn/PycharmProjects/LearnWithLlew/LearnWithLlew.jar"
sys.path.append(libDir)

from org.learnwithllew.teachingextensions.logo import Tortoise

def show():
    Tortoise.show()
