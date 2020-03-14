class IndexOutOfBound(Exception):
	pass
class array:
	def __init__(self, *args):
		self.dic = {}
		for i in range(len(args)):
			self.dic[i] = args[i]
	
	def __getitem__(self, index):
		try:
			if isinstance(index,int) and index>=len(self.dic):
				raise IndexOutOfBound
			return self.dic[index]
		except IndexOutOfBound:
			print('Index Out of Bound!')
	
	def __setitem__(self, index, value):
		try:
			if isinstance(index,int) and index>len(self.dic): 
				raise IndexOutOfBound
			# would let you insert one new element to the end
			self.dic[index] = value
		except IndexOutOfBound:
			print('Index Out of Bound!')	
			
	def __str__(self):
		elements = []
		for key in self.dic.keys():
			elements.append(str(self.dic[key]))
		string = ','.join(elements)
		return '['+string+']'

