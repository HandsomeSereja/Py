from functools import reduce
import csv

with open("data.csv","r") as file:
	keys = file.readline()
	reader = csv.reader(file, delimiter=",")
	dataset = [x for x in reader]
keys = list(keys.split(","))
USA = list(map(lambda x: x[2] == '', dataset))
print(USA.count(True))