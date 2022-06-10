class Operator:
	def __init__(self):
		self.l1=[]
	def getElements(self):
		length=int(input("Enter the length"))
		for i in range(0,length):
			ele=int(input("Enter the element"))
			self.l1.append(ele)
	def __mul__(self,others):
		zipl=zip(self.l1,others.l1)
		zipn=[]
		for m,n in zipl:
			zipn.append(m*n)
		print("The addition is", zipn)
