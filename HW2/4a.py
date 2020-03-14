def trace(func):
	func.indent = 1
	def call(*args):
		print('|'+('\t|'*(func.indent-1))+'-- '+func.__name__,*args)
		func.indent+=1
		rval = func(*args)
		func.indent-=1
		print('|'+('\t|'*(func.indent))+'-- return',rval)
		return rval
	return call

