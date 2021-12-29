import os
import socket

counter = 0
num = input("Enter a number between 1 to 9 :")
while (num.isdigit() is False) and counter <=1:
    print("Please enter number!!!")
    num=input("Enter a number between 1 to 9 :")
    counter = counter + 1

if counter <=1:
    nums =  int(num)
    if nums ==0:
        raise ValueError("Please dont enter zero")
    if nums ==1:
        directory =input("Enter you direcotry name :")
        parent_dir = "C:/"+input("\n Enter Location for your directory :")
        path = os.path.join(parent_dir, directory)
        try:
            os.makedirs(path, exist_ok=True)
            print("\n Directory '%s' created seccessfully"%directory)
        except OSError as error:
            print(error)
    if nums == 2:
        hostname = socket.gethostname()
        IPAddr = socket.gethostname(hostname)
        print("Your Computer Name is : " + hostname)
        print("your Computer IP Address is : "+ IPAddr)

    if nums ==3:
        shutdown = input("Do you want to shoutdown your pc? (yes/no):")
        if shutdown == 'no':
            exit()
        else:
            os.system("shutdown /s /t 1")
    if nums==4:
        os.system("start \"\" https://mrdoob.com/project/chromeexperiment/google-gravity/")
    if nums in range(5,10):
        class fiv:
            def __init__(self,a,b):
                self.a=a
                self.b=b
            def opn(self):
                ope = open("data.txt","w")
                a = self.a+self.b
                solve=[f"The solution of {self.a} and {self.b} is "+str(a)]
                ope.writelines(solve)
                ope=open("data.txt","r")
                print("The addition is :")
                print(ope.readline())
                print()
                ope.close()
        ans=fiv(int(input("first: ")),int(input("second:")))
        ans.opn()
    if nums>10:
        print("only digits\nNot Numbers \nTry next time")
else:
    print('Error: cannot exceed three attempts')
    exit()
    