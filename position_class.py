class Position:
	def __init__(self, position, applicants):
		self.candidates = {}
		self.position = position
		self.applicants = applicants
		self.set_up_votes(self.applicants)
		
	def set_up_votes(self, applicants):
		for applicant in self.applicants:
			self.candidates[applicant] = 0
	
	def make_vote(self, applicant_ind):
		candidate_name = self.applicants[applicant_ind]
		self.candidates[candidate_name] += 1
	
	def show_results(self):
		print(self.position.capitalize() + ':')
		for applicant, result in self.candidates.items():
			print(applicant, result)
		print('\n')

	def __str__(self):
		print(self.position.capitalize() + ':')
		for i in range(len(self.applicants)):
			print(str(i + 1) + '. ' + self.applicants[i])
		return ""
