from valid_members import obtain_valid_members
from important_algorithms import binarySearch
import pandas

def handle_unexpected_crashes():
	# USE FIREBASE
	pass

def show_progress():
	"""Show the election progress"""
	# create a file where it shows how election is going
	pass

def is_email_valid(email):
	# TODO: validate domain. Does it have to be a 'ualberta domain'

	# validate right characters
	# validate the email is in the mailing list:
	# valid members obtained from imported python file
	valid_members = obtain_valid_members()
	# validate time => specify until what time you accept answers 
	pass

def voting_menu():
	"""Start the voting process """
	# Show the candidates
	positions = {'president':['Chris', 'Lucky'], 'vp admin':['John', 'Lucky'], 'vp finance':['Cassandra','Lucky']}

	voted_members = [] # members who already voted
	# Initialize positions
	president = Position(positions['president'])
	vp_admin = Position(positions['vp admin'])
	vp_finance = Position(positions['vp finance'])

	# another menu where they can vote
	while True:
		email_inputted = input('Input your ualberta email to make a vote, or type \'EXIT\' to exit.\n')
		if email_inputted.upper() == 'EXIT':
			break
		if is_email_valid(email_inputted):			# validate email inputted
			# show vp positions
			pass
		print('We\'re sorry! You\'re not in the member list.\nPlease give let another member make a vote')
	# if email is valid, ask further details like name. 
	# 		add it to members who already voted
	#			update the votes of the candidates
	# when STOP is inputted, show_progress()
	pass

def main_menu():
	# Give 2 options
	# show progress
	# make a vote
	print('------- WELCOME TO THE ELECTION APP! -------')
	print("TYPE 1 OR 2 TO CHOOSE.")
	print("PRESS 'Q' TO QUIT ")
	functions = [show_progress, voting_menu]
	option = ''
	while True:
		# show options
		for i in range(0, len(functions)):
			print(str(i+1) + '). ' + functions[i].__doc__)
		option = input('> ')
		try:
			functions[int(option)-1]()
		except:
			if option.upper() == 'Q':
				break
			print("Invalid input. Please try again!\n\n")

class Position:
	def __init__(self, applicants):
		self.candidates = {}
		self.applicants = applicants
		self.set_up_votes(self.applicants)
		
	def set_up_votes(self, applicants):
		for applicant in self.applicants:
			self.candidates[applicant] = 0
	
	def make_vote(self, candidate_name):
		self.candidates[candidate_name] += 1


def main():
	main_menu()

main()