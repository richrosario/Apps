def collatz(number):
	if number % 2 == 0:
		print(number // 2)
		return number // 2
		
	elif number % 2 != 0:
		print((number * 3)+1)
		return (number * 3)+1


n = input("Enter a number: ")
while n != 1:
	n = collatz(int(n))
