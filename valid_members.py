from important_algorithms import heapSort, binarySearch
import pandas as pd
import time
###  ADD UNEXPECTED CRASHES

# MIGHT ADD NAMES IF NOT, DELETE DF
def data_extraction(filename, col_name):
	df = pd.read_csv(filename, skiprows=1)
	data = df[col_name]
	return data, df

# format list of attendees
def format_attendees(attendees):
	for i in range(0, len(attendees)):
		attendees[i] = attendees[i].strip().lower() # change it to capitalize for names

# obtains a sorted valid members
def obtain_valid_members():
	# ppl who are in the mailing list and  are obtained
	mailing_list_file = 'tutors.csv'
	mailing_col_name = 'Email address'
	mailing_list = data_extraction(mailing_list_file, mailing_col_name)
	mailing_list = mailing_list[0]

	# ppl who attended events
	event_list_file = 'events.csv'
	event_col_name = 'Email address'
	event_list, df = data_extraction(event_list_file, event_col_name)

	mailing_list = list(mailing_list)
	event_list = list(event_list)

	# create result file
	filename = 'valid_members.csv'
	valid_members = []
	valid = open(filename, 'w+')
	title = 'Valid Members\n'
	columns_names = 'Names, Emails\n'
	valid.write(title)
	valid.write(columns_names)

	# format the answers
	format_attendees(mailing_list)
	format_attendees(event_list)

	# Obtain the valid members
	for mailing_attendee in mailing_list:
		if mailing_attendee in event_list:
			valid.write(mailing_attendee+'\n')
			valid_members.append(mailing_attendee)
	return valid_members

if __name__ == '__main__':
	obtain_valid_members()