import sys
import math

class RightTriangle:
    # has an __init__ method that takes either two parameters(the two non-hypotenuse sides) or three (including the hypotenuse).
    def __init__(self, sideA, sideB, hypotenuse=None):
        # If only two parameters are sent,
        if hypotenuse == None:
            try:
                # set instance variables for the two sides and the hypotenuse
                self.sideA = float(sideA)
                self.sideB = float(sideB)
                # the hypotenuse is calculated using the Pythagorean theorem
                self.hypotenuse = math.sqrt(
                    math.pow(self.sideA, 2) + math.pow(self.sideB, 2)
                )
            except:
                raise Exception("Error: sides are not numbers")
            # raises exceptions if any of the parameters are negative
            if self.sideA <= 0 or self.sideB <= 0:
                raise Exception("Error: both sides must be nonnegative")
        else:
            try:
                # set instance variables for the two sides and the hypotenuse
                self.sideA = float(sideA)
                self.sideB = float(sideB)
                self.hypotenuse = float(hypotenuse)
            except:
                raise Exception("Error: sides are not numbers")
            # raises exceptions if any of the parameters are negative
            if self.sideA <= 0 or self.sideB <= 0 or self.hypotenuse <= 0:
                raise Exception(
                    "Error: both sides and the hypotenuse must be nonnegative"
                )
            # raise exceptions if the parameters are supplied but are not valid Pythagorean triple (ie, if it is not true that the a2 + b2 =  c2).
            if (
                # Test this using the technique involving absolute value
                abs(
                    self.hypotenuse
                    - math.sqrt(math.pow(self.sideA, 2) + math.pow(self.sideB, 2))
                )
                > 0.00001
            ):
                raise Exception("Error: not a valid pythagorean triple")

    # has an __eq__ method returns if the two sides of the other triangle are very close to the two sides of this triangle
    def __eq__(self, other):
        # uses the technique involving absolute value
        if abs(other.hypotenuse - self.hypotenuse) < 0.00001:
            return True
        # else, returns true
        else:
            return False

    # has a __str__ method that returns a string
    def __str__(self):
        return (
            "Right Triangle with side a = "
            + str(self.sideA)
            + ", side b = "
            + str(self.sideB)
            + ", and hypotenuse = "
            + str(self.hypotenuse)
        )


result1 = None
result2 = None
while result1 == None and result2 == None:
    # first, asks the user for two nonnegative numeric values for the sides
    a1 = input("Enter a nonegative numeric value for side A for rectangle 1: ")
    b1 = input("Enter a nonegative numeric value for side B for rectangle 1: ")
     
    try:
        r1 = RightTriangle(a1, b1)
        print(r1)
    # prints the Exception messages raised by the init method if the input is invalid
    except Exception as e:
        print(e)

    # does the same with three values
    a2 = input("Enter a nonegative numeric value for side A on rectangle 2: ")
    b2 = input("Enter a nonegative numeric value for side B on rectangle 2: ")
    hyp = input("Enter a nonegative numeric value for hyptoneuse on rectangle 2: ")
    
    try:
        r2 = RightTriangle(a2, b2, hyp)
        print(r2)
    except Exception as e:
        print(e)
    try:
        # shows whether the first triangle is equal to itself
        result1 = str(r1 == r2)
    except Exception as e:
        print(e)
    try:
        # then whether the first triangle is equal to the second one.
        result2 = str(r2 == r1)
    except Exception as e:
        print(e)

print(result1)
print(result2)