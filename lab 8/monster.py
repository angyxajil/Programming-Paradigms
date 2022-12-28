import sys

class Monster:
	def __init__(self, name, size):
		self._name = name
		self._size = size

	def attack(self, location):
		print(str(self._name) + " attacks " + str(location))

	def get_name(self):
		return self._name

	def get_size(self):
		return self._size
        
	def __str__(self):
		return str(self._name) + ' with size ' + str(self._size) + '.'

	def __eq__ (self, other):
		if((self._name == other._name) and (self._size == other._size)):
			return True
		else:
			return False
			
	def __add__(self, other):
		return Monster(self._name + other._name, self._size + other._size)

def main():
	monA = Monster("Godzilla",100)
	monA.attack("Italy")
	str(monA)
	print("\nMonster A name: " + str(monA.get_name()))
	print("Monster A size: " + str(monA.get_size()))

	monB = Monster("Godzilla",100)
	print("\nMonster A is the same as Monster B: " + str(monA == monB))

	monC = Monster("Kong",100)
	print("Monster A is the same as Monster C: " + str(monA == monC))

	monD = monA + monC
	print("\nMonster A + C: " + str(monD))

if __name__ == "__main__":
    sys.exit(main())