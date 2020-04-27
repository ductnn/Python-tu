class Person:
	def __init__(self, firstName, lastName, idN):
		self.firstName = firstName
		self.lastName = lastName
		self.idN = idN
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idN)

class Student(Person):
	"""docstring for Student"""
	def __init__(self, firstName, lastName, idN, scores):
		super().__init__(firstName, lastName, idN) #tính kế thừa
		self.scores = scores

	def cal(self):
		total = 0
		for scores in self.scores:
			total += scores
		avg = total/len(self.scores)

		if 90 <= avg <= 100: return 'O'
		if 80 <= avg < 90: return 'E'
		if 70 <= avg < 80: return 'A'
		if 55 <= avg < 70: return 'P'
		if 40 <= avg < 55: return 'D'
		return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idN = line[2]
nScores = int(input())
scores = list(map(int, input().split())) #list scores
s = Student(firstName, lastName, idN, scores)
s.printPerson()
print("Grade:", s.cal())
