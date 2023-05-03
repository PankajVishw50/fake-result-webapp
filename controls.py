


with open('templates/data.txt', 'wb') as file:
	for x in range(1000000):
		file.write(str(x).encode())