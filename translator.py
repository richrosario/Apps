#Chisca Language
# vowels become ->g 

#dog -> dgg
#cat -> cgt 



def translate(phrase):
	translated = ""
	for letter in phrase:
		if letter in "AEIOUaeiou":
			translated = translated + 'g'
		else:
			translated = translated + letter
	return translated

print(translate(input("Enter a word: ")))