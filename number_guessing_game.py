import random

num = random.randint(1,6)
count = 0
print("Take a guess")


for x in range(6):
	guess = int(input())

	if guess == num:
		print("Good guess you guessed in " + str(count) + " times!!")
		break
	elif guess < num:
		print("Too low of a guess")
		count += 1
	elif guess > num:
		print("Too high of a guess")
		count += 1

print("You failed, the number was " + str(num))