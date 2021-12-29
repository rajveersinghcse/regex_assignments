import os
import socket 


counter = 0
num=input("Enter a digit in between 1-9 :  ")


while (num.isdigit() is False) and counter <= 1:
    print('You cannot enter a string!')
    num=input("Enter a digit in between 1-9 :  ")
    counter = counter + 1
    

if counter <= 1:
    nums = int(num)
    
    if nums == 0:
        raise ValueError('Enter other than ZERO')
    
    if nums ==1:
        directory=input("Enter your new directory name:   ")
        parent_dir="C:/"+input("\nEnter Location for your directory: ")
        path = os.path.join(parent_dir, directory)
        
        try:
            os.makedirs(path, exist_ok = True)
            print("\nDirectory '%s' created successfully" % directory)
        
        except OSError as error:
            print(error)
    
    if nums==2:
        hostname = socket.gethostname()   
        IPAddr = socket.gethostbyname(hostname)    
        print("Your Computer Name is:" + hostname)   
        print("Your Computer IP Address is:" + IPAddr)  
    
    if nums==3:
        shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")
        if shutdown == 'no':
            exit()
        else:
            os.system("shutdown /s /t 1")
    
    if nums==4:
        os.system("start \"\" https://mrdoob.com/projects/chromeexperiments/google-gravity/")
    
    if nums in range(5,10):
        class fiv:
            def __init__(self,a,b):
                self.a=a
                self.b=b
            def opn(self):
                ope=open("data.txt","w")
                a=self.a+self.b
                solve=[f"The solution of {self.a} and {self.b} is "+ str(a)]  
                ope.writelines(solve)
                ope.close()
                ope=open("data.txt","r")
                print("The addition is: ")
                print(ope.readline())
                print()
                ope.close()
        ans= fiv(int(input("first:")),int(input("second:")))
        ans.opn()
    
    if nums>=10:
        print("Only digits\nNot numbers \nBetterluck nexttime")
            
        
        

else:
    print('Error: cannot exceed three attempts')
    exit()
