#self parametro(variable publica interna)

class Coder():
	def __init__(self, name):
		self.Name = name

	def info_println(self):
		print(self.Name)
	
	def is_pythonner(self):
		if 'Python' in self.language:
			print(True)
		else:
			print(False)

cd = Coder('Ale')
cd.info_println()
cd.language = ['Python','C']
print(cd.is_pythonner())
del(cd.language)