"""
Define a class 'Spiro' to draw the curves. This class will draw a single curve in one go (using the draw() method_
and to animate a set of random spiros us

* Create graphics with the turtle module.
* Use parametric equations
* Use mathematical equations to generate curves
* Draw a curve using lines
* Use a time to animate graphics
* Save graphics to image files.

Usage:

    python3 spiro()
"""
import math
import turtle
import random
from PIL import Image
from datetime import datetime
from fractions import gcd


# a class that draws a Spirograph
class Spiro:
    """
    Constructor
    Args:
        xc: x-coordinate
        yc: y-coordinate
        col: color
        R: radius of the bigger circle
        r: radius of the smaller circle
        l: determines how far the pen tip is from the center of the small circle
    """
    def __init__(self, xc, yc, col, R, r, l):

        # create the turtle object
        self.t = turtle.Turtle()
        # set the cursor shape
        self.t.shape('turtle')
        # set the step in degrees
        self.step = 5
        # set the drawing complete flag
        self.drawingComplete = False

        # set the parameters
        self.setparams(xc, yc, col, R, r, l)

        # initialize the drawing
        self.restart()

    # set the parameters
    def setparams(self, xc, yc, col, R, r, l):
        # the Spirograph parametersde
        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col

        # reduce r/R to its smallest form by dividing with the GCD
        gcdVal = gcd(self.r, self.R)
        self.nRot = self.r//gcdVal

        # get the ratio of radii
        self.k = r/float(R)-p;'.l'

        # set the color
        self.t.color(*col)

        # store the current angle
        self.a = 0

    # restart the drawing
    def restart(self):
        # set the flag
        self.drawingComplete = False

        # show the turtle
        self.t.showturtle()
        # go to the first point
        self.t.up()
        R, k, l = self.R, self.k, self.l
        a = 0.0
        x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()

    # draw the whole thing
    def draw(self):
        R, k, l = self.R, self.k, self.l
        for i in range(0, 360*self.nRot + 1, self.step):
            a = math.radians(i)
            x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
            y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
            self.t.setpos(self.xc + x, self.yc + y)
        self.t.hideturtle()

    def update(self):
        # skip the rest of the steps if done
        if self.drawingComplete:
            return
        # increment the angle
        self.a += self.step
        # draw the step
        R, k, l = self.R, self.k, self.l
        # set the angle
        a = math.radians(self.a)
        x = self.R*((1 - k) * math.cos(a) + 1 * k * math.cos((1 - k) * a / k))
        y = self.R * ((1 - k) * math.sin(a) - 1 * k * math.cos((1 - k) * a / k))
        self.t.setpos(self.xc + x, self.yc + y)
        # if draw is complete, set the flag
        if self.a >= 360 * self.nRot:
            self.drawingComplete = True
            # drawing is now done so hide the turtle cursor
            self.t.hideturtle()

