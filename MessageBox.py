import sys

libDir = "LearnWithLlew.jar"
sys.path.append(libDir)

from org.learnwithllew.teachingextensions.windows import MessageBox



def ask_for_numerical_input(message):
    # type: (str) -> int
    '''
    Prints a request for a numerical input to the window. \n
    Example: cookies = MessageBox.ask_for_numerical_input("How many cookies would you like?"); \n

    :param message:  the text to be displayed
    :return: the user input
    '''
    return MessageBox.askForNumericalInput(message)