import sys

# Counts the letters in the string by stripping 
# the first letter recursively and returning a count,
# which increases as the recursion unwinds. 
# Works with a string of length 0. 
def count(data):
    amount = 0
    if (len(data) == 0):
        return amount
    
    # Returns the int length.
    amount += 1
    return amount + count(data[1:]) 

# Reverses the letters in the string by stripping
# the first letter in each recursive call, then adding
# them to end of a new string as the recursion unwinds. 
def reverse(data):
    if(len(data) == 0):
        return ""
    
    # Returns the reversed string.
    return reverse(data[1:]) + data[0]

# Determine whether the string is a palindrome by stripping the first and last letters in each instance of the function and comparing them for equality. 
# Termination condition for recursion works correctly for strings of both odd and even lengths.
# Converts all letters to lower case with lower() and use isalpha() to ignores punctuation and blanks. 
# Returns a boolean
def isPalindrome(data):
    if (len(data) <= 1):
        return True

    if (data[0].isalpha() == data[-1].isalpha()):
        return True
    else:
        return False
        
    return isPalindrome(data[1:-1])
        

def main():
    data = input("Enter a string: ")
    print("Length: " + str(count(data)))
    print("Reversed String: " + str(reverse(data)))

    print("Palindrome: " + str(isPalindrome(data)))

if __name__ == "__main__":
    sys.exit(main())