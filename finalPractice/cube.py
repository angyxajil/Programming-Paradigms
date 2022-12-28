import math
import sys

class Cube:

    def __init__(self, side_length = 0):
        try:
            if self._side_length < 0 :  
                print ("side length must not be nonnegative")
        except:
            self._side_length = float(side_length)
            self._volume = self._side_length * 3

    def __eq__(self, other):
        if other == None:
            return False

        elif ((other._volume - self._volume) < .001):
            return True
        
        else:
            return False

    def __add__ (self, other):
        combined_vol = self._volume + other._volume
        return "Cube with volume " + str(combined_vol * .33333)

    def __str__(self):
        return "Cube with side = " + str(self._side_length) + " and volume " + str(self._volume)

def main():
    while(True):
        try: 
            s1 = float(input("please enter a non negative float for the length of one side of cube 1: "))
            c1 = Cube(s1)
            print(c1)
            break
        except:
            print("Side length must be a valid float")

    while(True):
        try: 
            s2 = float(input("please enter a non negative float for the length of one side of cube 2: "))
            c2 = Cube(s2)
            print(c2)
            break
        except:
            print("Side length must be a valid float")

    print(c1.__eq__(c1))
    print(c1.__eq__(c2))
    print(c1.__add__(c2))

if __name__ == "__main__":
    sys.exit(main())