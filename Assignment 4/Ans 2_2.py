#Check the nanem is Palindrome or not. not using slicing

name = input("Enter the name :")
def isPalindrome(name):
 
    for i in range(0, int(len(name)/2)):
        if name[i] != name[len(name)-i-1]:
            return False
    return True
 
pal = isPalindrome(name)
 
if pal:
    print("The name is Palindrome")
else:
    print("The name is not Palindrome")