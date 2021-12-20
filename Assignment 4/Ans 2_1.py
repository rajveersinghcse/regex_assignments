from os import rename


#Ans 2: Check the nanem is Palindrome or not using indexing & slicing

name = list(input("Enter the name :"))
def isPalindrome(name):
    return name == name[::-1]
pal = isPalindrome(name)
if pal:
    print("The name is Palindrome")
else:
    print("The name is not Palindrome")



