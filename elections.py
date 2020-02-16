from valid_members import obtain_valid_members
from position_class import Position
import pandas, os
import sqlite3
import sys

# connect database
def connect_database(path):
	global conn, cursor

	# if the file already exists, don't create a table
	try:
		open(path, 'r')
		query = ''
	except OSError:
		query = "CREATE TABLE election (email TEXT, PRIMARY KEY(email));"
	finally:
		conn = sqlite3.connect(path)
		cursor = conn.cursor()
		cursor.execute(query)
		conn.commit()

	cursor.execute('PRAGMA foreign_keys=ON; ')
	conn.commit()
	return

def clear():
	os.system('cls' if os.name=='nt' else 'clear')

def show_progress(position_obj={}):
	"""Show the election progress"""
	if not bool(position_obj):
		print('No votes have been made\n')
		return
	# TODO: create a file where it shows how election is going
	return

# Validate the email inputted
# returns if it's valid and gives a warning 
def is_email_valid(email):
	# TODO: Does it have to be a 'ualberta domain'
	is_email_valid = True
	cursor_valid_members = obtain_valid_members()
	
	# validate right characters
	email_char = email.split('@')
	
	query = "SELECT email from valid_members_table WHERE email = '{}';".format(email)
	cursor_valid_members.execute(query)
	valid_members = cursor_valid_members.fetchone()
	

	if len(email_char) != 2:
		message = 'Invalid email. Try again. Press enter to continue.\n'
		is_email_valid = False
	
	# validate the domain
	elif email_char[-1] != 'ualberta.ca':
		message = 'Invalid email domain. Use your ualberta email.\n'
		is_email_valid = False

	# validate the email is in the mailing list
	elif valid_members is None:
		message = 'We\'re sorry! You\'re not in the member list.\nPlease let another member vote, and press enter to continue.\n'
		is_email_valid = False
	# if none of the other conditions are met, the email is valid
	else:
		message = 'CONGRATS!!! YOU HAVE VOTED! PRESS ANY ENTER TO CONTINUE\n'
	return is_email_valid, message

# returns the position object
def voting_menu():
	"""Start the voting process """
	global conn, cursor
	clear()
	# Show the candidates
	raw_positions = {'president':['Chris', 'Lucky'], 'vp_admin':['Nancy', 'Lucky'], 'vp_finance':['Cassandra','Lucky']}

	# positions
	positions_obj = []

	# Initialize positions
	for position in raw_positions:
		obj = Position(position, raw_positions[position], cursor, conn)
		positions_obj.append(obj)

	# another menu where they can vote
	while True:
		email_inputted = input('Input your ualberta email to make a vote, or type \'Q\' to quit.\n> ').strip()
		print('\n')
		if email_inputted.upper() == 'Q':
			# TODO: DELETE THIS
			for position in positions_obj:
				position.show_all_results()
			break
		is_valid, message = is_email_valid(email_inputted)

		if is_valid:
			# record members who voted check if they have not already voted
			try:
				query = "INSERT INTO election VALUES ('{}');".format(email_inputted)
				cursor.execute(query)
				conn.commit()

				# print options
				for position in positions_obj:
					print(position)
					# handle exceptions for option
					while True:
						option = input('Choose a candidate by selecting a number\n> ').strip()
						print('\n')
						try:
							position.make_vote(int(option) - 1)
							break
						except:
							print('Invalid input. Try again.\n')
			except:
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
	functions = [show_progress, voting_menu]
	
	option = ''
	while True:
		print("TYPE 1 OR 2 TO CHOOSE.")
		print("PRESS 'Q' TO QUIT ")
		# show options
		for i in range(0, len(functions)):
			print(str(i+1) + '). ' + functions[i].__doc__)
		# handle input
		option = input('> ')
		# handle option error
		try:
			functions[int(option)-1]()
		except SystemExit:
			print("Exiting...")
			sys.exit()
		except:
			if option.upper() == 'Q':
				break
			print("Invalid input. Please try again!\n\n")

def main():
	global conn, cursor
	path = './election.db'
	connect_database(path)
	main_menu()

main()
