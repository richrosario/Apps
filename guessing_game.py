secret_word = "giraffe"
tries = 10

while tries >= 0:
	guess = input("Guess a word!")
	if guess == secret_word:
		print("You guessed right CONGRATS!!!")
		exit()
	else:
		if tries == 0:
			print("YOU LOSE")
			exit()
		else:

			print("WRONG, try again")
			print("You have " + str(tries) + " tries left")
			tries = tries - 1
#