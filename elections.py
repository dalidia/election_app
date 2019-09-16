from valid_members import obtain_valid_members
from important_algorithms import binarySearch
from position_class import Position
import pandas, os

def handle_unexpected_crashes():
	# USE FIREBASE
	pass

def clear():
	os.system('cls' if os.name=='nt' else 'clear')

def show_progress(position_obj={}):
	"""Show the election progress"""
	if not bool(position_obj):
		print('No votes have been made\n')
		return
	# create a file where it shows how election is going
	return

# Validate the email inputted
# returns if it's valid and gives a warning 
def is_email_valid(email):
	# TODO: Does it have to be a 'ualberta domain'
	is_email_valid = True
	valid_members = obtain_valid_members()
	
	# validate right characters
	email_char = email.split('@')
	
	if len(email_char) != 2:
		message = 'Invalid email. Try again. Press any key to continue.\n'
		is_email_valid = False
	
	# validate the domain
	elif email_char[-1] != 'ualberta.ca':
		message = 'Invalid email domain. Use your ualberta email.\n'
		is_email_valid = False

	# validate the email is in the mailing list
	elif email not in valid_members:
		message = 'We\'re sorry! You\'re not in the member list.\nPlease let another member vote, and press any key to continue.\n'
		is_email_valid = False
	# if none of the other conditions are met, the email is valid
	else:
		message = 'CONGRATS!!! YOU HAVE VOTED! PRESS ANY KEY TO CONTINUE\n'
	return is_email_valid, message

# returns the position object
def voting_menu():
	"""Start the voting process """
	clear()
	# Show the candidates
	raw_positions = {'president':['Chris', 'Lucky'], 'vp admin':['John', 'Lucky'], 'vp finance':['Cassandra','Lucky']}
	
	# members who already voted
	voted_members = [] 

	# positions
	positions_obj = []

	# Initialize positions
	for position in raw_positions:
		obj = Position(position, raw_positions[position])
		positions_obj.append(obj)

	# another menu where they can vote
	while True:
		email_inputted = input('Input your ualberta email to make a vote, or type \'Q\' to quit.\n> ')
		print('\n')
		if email_inputted.upper() == 'Q':
			for position in positions_obj:
				position.show_results()
			break
		has_voted = email_inputted in voted_members
		is_valid, message = is_email_valid(email_inputted)

		# validate email inputted and check if it has not already voted
		if is_valid and not has_voted:
			# show exec positions
			voted_members.append(email_inputted)
			# print options
			for position in positions_obj:
				print(position)
				# handle exceptions for option
				while True:
					option = input('Choose a candidate by selecting a number\n> ')
					print('\n')
					try:
						position.make_vote(int(option) - 1)
						break
					except:
						print('Invalid input. Try again.\n')

		elif has_voted:
			message = "We\'re sorry! You have already voted. Please let another member vote and press any key to continue.\n"
		input(message)
		clear()
	# if email is valid, ask further details like name. 
	# 		add it to members who already voted
	#			update the votes of the candidates
	# when STOP is inputted, show_progress()
	return

def main_menu():
	# Give 2 options
	# show progress
	# make a vote
	clear()
	print('------- WELCOME TO THE ELECTION APP! -------')
	print("TYPE 1 OR 2 TO CHOOSE.")
	print("PRESS 'Q' TO QUIT ")
	functions = [show_progress, voting_menu]
	
	option = ''
	while True:
		# show options
		for i in range(0, len(functions)):
			print(str(i+1) + '). ' + functions[i].__doc__)
		# handle input
		option = input('> ')
		# handle option error
		try:
			functions[int(option)-1]()
		except:
			if option.upper() == 'Q':
				break
			print("Invalid input. Please try again!\n\n")

def main():
	main_menu()

main()