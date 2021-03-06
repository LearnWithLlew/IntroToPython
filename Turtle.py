import sys

libDir = "LearnWithLlew.jar"
sys.path.append(libDir)

from org.learnwithllew.teachingextensions.logo import Tortoise

def show():
    '''
    Displays the Turtle \n
    Example: Turtle.show()
    '''
    Tortoise.show()
def set_speed(speed):
    '''
    Sets the speed the tortoise moves \n
    Example:  Tortoise.set_speed(8) \n
    :param speed:
             The speed from 1 (slowest) to 10 (fastest)
   '''
    Tortoise.setSpeed(speed)

def move(lengthInPixels):
    '''
    Moves the Tortoise Forward the number of pixels specified.\n
    Example: Tortoise.move(72) \n
    :param lengthInPixels:
             The number of pixels to move. Negative numbers will move the
             Tortoise backwards.
    '''
    Tortoise.move(lengthInPixels)

def turn(degreesToTheRight):
    '''
    Turns the Tortoise to the right (clockwise) the degrees specified. \n
    Example: Tortoise.turn(90) \n
    :param degreesToTheRight:
             The degrees to turn. Negative numbers will move the Tortoise to
             the left (counter-clockwise)
    '''
    Tortoise.turn(degreesToTheRight)

def set_pen_color(color):
    # type: (Colors) -> None
    '''
    Sets the color drawn by the Tortoise. \n
    Tortoise.setPenColor(Colors.Reds.Red) \n
    see Colors \n
    :param color:
       the color of the pen
    '''
    Tortoise.setPenColor(color)

def set_pen_width(width_in_pixels):
    '''
    Sets the width of the pen drawn by the Tortoise. \n
    Example:  Tortoise.set_pen_width(2) \n
    :param width_in_pixels:
             the width of the pen stroke
    '''
    Tortoise.setPenWidth(width_in_pixels)
    '''
  /**
   * Gets the speed that the tortoise moves
   * <div><b>Example:</b> {@code int speed =  Tortoise.getSpeed();}</div>
   *
   * @return the speed the Tortoise is currently set to
   */
  public static int getSpeed()
  {
    return turtle().getSpeed();
  }



  /**
   * Sets the width of the pen drawn by the Tortoise. <br/>
   * <div><b>Example:</b> {@code  Tortoise.setPenWidth(2)}</div>
   *
   * @param width
   *          the width of the pen stroke
   */
  public static void setPenWidth(Number width)
  {
    turtle().setPenWidth(width.intValue());
  }
  /**
   * Gives you access to the window the
   * Tortoise is moving on so you can do things like change it's color. <br/>
   * <b>Example:</b> {@code  TurtlePanel panel = Tortoise.getBackgroundWindow()}
   */
  public static TurtlePanel getBackgroundWindow()
  {
    return turtle().getBackgroundWindow();
  }
  /**
   * Gets the current width of the pen drawn by the Tortoise. <br/>
   * <div><b>Example:</b> {@code  width = Tortoise.getPenWidth()}</div>
   *
   * @return the width of the pen stroke
   */
  public static int getPenWidth()
  {
    return turtle().getPenWidth();
  }
  /**
   * Gets the current color of the pen drawn by the Tortoise. <br/>
   * <div><b>Example:</b> {@code  pen = Tortoise.getPenColor()}</div>
   *
   * @return the color of the pen stroke
   */
  public static Color getPenColor()
  {
    return turtle().getPenColor();
  }
  /**
   * Sets the position of the Tortoise on the y axis. <br/>
   * (0,0) is the top left of the screen <br/>
   * <div><b>Example:</b> {@code  Tortoise.setY(30);}</div>
   *
   * @param y
   *          the position in pixels of the Tortoise on the Y axis
   */
  public static void setY(int y)
  {
    turtle().setY(y);
  }
  /**
   * Sets the position of the Tortoise on the x axis. <br/>
   * (0,0) is the top left of the screen <br/>
   * <div><b>Example:</b> {@code  Tortoise.setX(30);}</div>
   *
   * @param x
   *          the position in pixels of the Tortoise on the X axis
   */
  public static void setX(int x)
  {
    turtle().setX(x);
  }
  /**
   * Gets the current position of the Tortoise on the y axis. <br/>
   * (0,0) is the top left of the screen <br/>
   * <div><b>Example:</b> {@code  y = Tortoise.getY()}</div>
   *
   * @return y the position in pixels of the Tortoise on the Y axis
   */
  public static int getY()
  {
    return turtle().getY();
  }
  /**
   * Gets the current position of the Tortoise on the x axis. <br/>
   * (0,0) is the top left of the screen <br/>
   * <div><b>Example:</b> {@code  x = Tortoise.getX()}</div>
   *
   * @return x the position in pixels of the Tortoise on the X axis
   */
  public static int getX()
  {
    return turtle().getX();
  }
  /**
   * Gets the current heading of the Tortoise. <br/>
   * 0 degrees is due north. <br/>
   * 90 degrees is due east. <br/>
   * <div><b>Example:</b> {@code  angle = Tortoise.getAngleInDegrees()}</div>
   *
   * @return the angle in degrees of the Tortoise
   */
  public static double getAngle()
  {
    return turtle().getAngleInDegrees();
  }
  /**
   * Changes the type of animal you are using. <br/>
   * <div><b>Example:</b> {@code  Tortoise.setAnimal(Animals.Spider);}</div>
   *
   * @return the angle in degrees of the Tortoise
   * @see Animals
   */
  public static void setAnimal(Animals animal)
  {
    turtle().setAnimal(animal);
  }
  /**
   * Makes it so the tortoise will not draw a line of color out of it's butt. <br/>
   * <b>Example:</b> {@code  Tortoise.penUp()}
   */
  public static void penUp()
  {
    turtle().penUp();
  }
  /**
   * Makes it so a line of color out of will trail from the Tortoise. <br/>
   * <b>Example:</b> {@code  Tortoise.penDown()}
   */
  public static void penDown()
  {
    turtle().penDown();
  }
  /**
   * Removes everything from the window. <br/>
   * <b>Example:</b> {@code  Tortoise.clear()}
   */
  public static void clear()
  {
    turtle().clear();
  }
  /**
   * Hides the tortoise, you will still see the pen markings it made before and after it hid. <br/>
   * <b>Example:</b> {@code  Tortoise.hide()}
   */
  public static void hide()
  {
    turtle().hide();
  }
  private static Turtle turtle()
  {
    return TortoiseUtils.getTurtle();
  }
  /**
   * Sets the angle the Tortoise is facing. <br/>
   * 0 is straight up (like 'North') <br/>
   * <div><b>Example:</b> {@code  Tortoise.setAngle(42);}</div>
   *
   * @param angle
   *          the angle in degrees
   */
  public static void setAngle(int angle)
  {
    turtle().setAngleInDegrees(angle);
  }
  public static void moveTo(int x, int y)
  {
    turtle().moveTo(x, y);
  }
}

'''
