class Code():
	def __init__(self, name):
		self.name = name
	def get_lang(self, long):
		self.lang = lang

def is_python(lst):
	if'Python' in lst:
		print(True)
	else:
		print(false)

cd = Code('KJ')
cd.get_lang(['Python','C'])
is_python(cd.lang) 