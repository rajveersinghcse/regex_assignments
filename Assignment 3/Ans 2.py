
#Ans 2:


emailid  = "arjun.yadav@gmail.com"
s1 = str(emailid.split(".", 1))
s2 = s1.split("@",1)
print(s2)