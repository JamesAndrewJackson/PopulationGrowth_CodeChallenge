from random import randint

f = open('years.txt', 'w')
for i in range(1000):
	date = randint(0,99)
	f.write(str(date + 1900) + " ")
	age = randint(1,100-date)
	f.write(str(date + age + 1900) + "\n")
f.close()
	