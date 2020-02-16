class Position:
	def __init__(self, position, applicants, cursor, conn):
		self.candidates = {}
		self.position = position
		self.applicants = applicants
		self.cursor = cursor
		self.conn = conn
		self.set_up_votes(self.applicants)
		
	def set_up_votes(self, applicants):
		# check if table already exists
		try:
			query = "CREATE TABLE {} (name TEXT, count INTEGER, PRIMARY KEY(name));".format(self.position)
			self.cursor.execute(query)

			for applicant in self.applicants:
				query = "INSERT INTO {} VALUES ('{}', 0);".format(self.position, applicant)
				self.cursor.execute(query)
			self.conn.commit()
		except:
			pass
	
	def make_vote(self, applicant_ind):
		candidate_name = self.applicants[applicant_ind]
		query = "UPDATE {} SET count = count + 1 WHERE name='{}'".format(self.position, candidate_name)
		self.cursor.execute(query)
		self.conn.commit()
	
	def show_all_results(self):
		print(self.position.capitalize() + ':')
		for applicant, result in self.candidates.items():
			print(applicant, result)
		print('\n')

	def __str__(self):
		print(self.position.capitalize() + ':')
		for i in range(len(self.applicants)):
			print(str(i + 1) + '. ' + self.applicants[i])
		return ""
