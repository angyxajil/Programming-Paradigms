def conversion(tempC):
	tempF = (tempC * 9.0/5.0) + 32
	return tempF
	
def main():
	min = int(input('Minimum temp: '))
	max = int(input('Maximum temp: '))

	print("Celsius	Fahrenheit")

	for tempC in range(min, max + 1):
		tempF = conversion(tempC)
        
		print(str(tempC)+"	"+str(tempF))

main()