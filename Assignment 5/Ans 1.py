class val:
	def __init__(self, x):
		self.x = x
	def __eq__(self, other):
		if(self.x == other.x):
			return True
		else:
			return False
				
a = int(input("Enter the first value :"))
b = int(input("Enter the second value :"))
y = val(a)
z = val(b)
print(y == z)
