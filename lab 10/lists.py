import sys

def list():
    list = [1, 2, 3, 4]
    return "Original list: " + str(list) + "\nCubed List: " + str([pow(num, 3) for num in list])

def fv(principal, rate, time):
    curr = principal * ((1 + rate) ** time)
    return curr

def listComp():
    tuples = [(1, 0.05, years) for years in range(1, 101)]
    return [fv(principal, rate, time) for principal, rate, time in tuples]

def lower(string):
	lowerList = [letter for letter in string if letter >= 'a' and letter <= 'z']
	lowerLetters = ''

	for letter in lowerList:
			lowerLetters += letter
	return lowerLetters

def main():
    print(list())

    tuples = [(70, 0.05, 1), (150, 1.05, 2), (30, 2, 3)]
    print("\nList of Tuples: " + str(tuples))
    print("Applied fv(): " + str([fv(principal, rate, time) for principal, rate, time in tuples]))

    print("\nList Comprehension to create tuples: " + str(listComp()))

    print("\nLower Case Letters: " + str(lower("She BElieVEd")))

if __name__ == "__main__":
    sys.exit(main())