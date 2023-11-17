import json
from random import choice, randint

def write(data, filename):
	data = json.dumps(data)
	data = json.loads(str(data))
	with open(filename, 'w', encoding = 'UTF-8') as file:
		json.dump(data, file)


def read(filename):
	with open(filename, 'r', encoding = 'UTF-8') as file:
		return json.load(file)


class Jacket():
	def __init__(self):
		self.brand = choice(['Adidas','TheNorthFace','Puma','Molotov','Zara'])
		self.color = choice(['black','white','blue','green','red'])
		self.size = choice(['XS','S','M','L','XL','XXL'])

data = {
	'Jacket': []
}

for i in range(5):
	data['Jacket'].append(Jacket().__dict__)

write(data,'shop.json')

n_data = read('shop.json')

for i in range(5):
	print(n_data['Jacket'][i])