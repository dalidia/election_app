import pandas as pd
import sqlite3
import os
import sys
# CHANGE THE LABEL OF EMAIL ADDRESS TO Email_address

def set_up_database():
	database = 'valid_members.db'
	try:
		query = ''
		os.remove(database)
	except:
		pass
	finally:
		query = ''' CREATE TABLE valid_members_table
										(valid_members TEXT, email TEXT, 
										PRIMARY KEY(email));'''
		# create database
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute(query)
		conn.commit()
	return conn, cursor

# MIGHT ADD NAMES IF NOT, DELETE DF
def data_extraction(filename, col_name):
	df = pd.read_csv(filename, skiprows=1)
	data = df[col_name]
	return data, df

# format list of attendees
def format_attendees(attendees):
	for i in range(0, len(attendees)):
		attendees[i] = attendees[i].strip().lower() # change it to capitalize for names

# obtains a list of valid members
def obtain_valid_members():
	conn, cursor = set_up_database()
	
	try:
		# ppl who are in the mailing list and  are obtained
		mailing_list_file = 'mailing_list.csv'
		mailing_col_name = 'Email_address'
		mailing_list = data_extraction(mailing_list_file, mailing_col_name)
		mailing_list = mailing_list[0]
	except:
		print("Problem opening {}".format(mailing_list_file))
		sys.exit()

	try:
		# ppl who attended events
		event_list_file = 'events.csv'
		event_col_name = 'Email_address'
		# df for obtain the name
		event_list, df = data_extraction(event_list_file, event_col_name)
	except:
		print("Problem opening {}".format(event_list_file))
		sys.exit()

	mailing_list = list(mailing_list)
	event_list = list(event_list)

	# format the answers
	format_attendees(mailing_list)
	format_attendees(event_list)

	# Obtain the valid members
	for mailing_attendee in mailing_list:
		if mailing_attendee in event_list:
			# obtain the name of the email address
			valid_name = df[df.Email_address == mailing_attendee].iloc[0,1]
			query = "INSERT INTO valid_members_table VALUES ('{}', '{}');".format(valid_name, mailing_attendee)
			try:
				cursor.execute(query)
			except:
				pass
	conn.commit()
	return cursor

if __name__ == '__main__':
	obtain_valid_members()
