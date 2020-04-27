from abc import ABC,abstractmethod

class PersonAbs(ABC):
	"""docstring for PersonAbs"""
	name = None
	age = 0
	def getName(self):
		print(self.name)
	def getAge(self):
		print(self.age)
	@abstractmethod
	def getFull(self):
		pass

class Person(PersonAbs):
    name = 'ductn'
    age = 21
    def getFull(self):
        self.getName()
        self.getAge()

Person().getFull();
