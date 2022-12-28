import sys

class Mess():

    # an init method that takes a sizeInSqM for the mess and sets an instance variable
    def __init__(self, sizeInSqM):
        self.size = sizeInSqM

    # an __eq__ method that overloads the == operator and returns true if the other Mess has the same size 
    #as the current one, otherwise returns false.  
    #Use the technique involving absolute value, not the == operator, to compare the sizes.
    def __eq__(self, temp):
        if((abs(self.size) == abs(temp.size))):
            return True
        else:
            return False

    #an __add__ method that overloads the + operator and returns a new Mess with the combined
    # sizeInSqM of the two old messes.
    def __add__(self, temp):
        return Mess(self.size + temp.size)
    
    #a __sub__ method that overloads the - operator and returns a new Mess whose size is the size of
    #the current Mess minus the size of the other Mess, but not less than zero (in other words,
    #if the other Mess was larger than the current one, return a new Mess of length 0)
    def __sub__(self, temp):
        if(self.size < temp.size):
            return Mess(0)
        else:
            return Mess(self.size - temp.size)
    
    #a __str__ method that return a string similar to this one: "Mess with size 5 square meters"
    def __str__(self):
            return f"Mess with size {self.size} square meter(s)"

def main():
    m1 = Mess(5)
    print("Mess 1: " + str(m1))

    m2 = Mess(10)
    print("Mess 2: " + str(m2))

    print("Mess 1 + Mess 2 : " + str(m1 +  m2))   
    print("Mess 1 - Mess 2 : " + str(m1 -  m2))
    print("Mess 2 - Mess 1 : " + str(m2 - m1))
    print("Mess 1 is the same size as Mess 2: " + str(m1 == m2))

    m3 = Mess(5)
    print("Mess 3 is the same size as Mess 1: " + str(m3 == m1))

if __name__ == "__main__":
    sys.exit(main())