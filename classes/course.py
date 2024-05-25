class Course:

	def __init__(self, name, skills, description):
		# note que neste exemplo, todos os atributos são públicos
		self.name = name
		self.description = description
		self.skills = skills
	
	def get_name(self):
		return self.name
	
	def get_skills(self):
		return self.skills
	
	def get_description(self):
		return self.description