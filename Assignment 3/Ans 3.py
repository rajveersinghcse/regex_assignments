
#Ans 3:


emailid  = "firstname.lastname.1995@gmail.com"
s1 = str(emailid.split(".", 2))
s2 = s1.split("@",1)
print(s2)