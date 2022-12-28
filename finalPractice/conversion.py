def conversion (cent):
    inches = cent * 2.54
    return inches

def main() :
    centimeters = [2.0, 2.0, 2.0]
    list = [conversion(cent) for cent in centimeters]
    tuple = [(cent, conversion(cent)) for cent in centimeters]

    print(list)
    print(tuple)

if __name__ == "__main__":
    main() 