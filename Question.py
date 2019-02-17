from Question import Question

question_prompts = [

	"What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Yellow\n\n",
	"What color are bananas?\n(a) Red/Green\n(b) Purple\n(c) Yellow\n\n",
	"What color are strawberries?\n(a) Red/Green\n(b) Purple\n(c) Yellow\n\n"
]

questions = [

	Question(question_prompts[0],"a"), #array of question objects 
	Question(question_prompts[1],"c"), #[1] meaning second one up above
	Question(question_prompts[2],"a")
]

def run_test(questions): #takes a list of questions objects 
	score = 0
	for question in questions:
		answer = input(question.prompt)
		if answer == question.answer:
			score += 1
	print("You answerd " + str(score) + " right out of " + str(len(questions)))


run_test(questions)

#Class below in seperate file 

''' 

class Question:
	def __init__(self, prompt, answer):
		self.prompt = prompt
		self.answer = answer

'''