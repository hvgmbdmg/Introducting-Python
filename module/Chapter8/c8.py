from ..common import common as c

def introduction():
	print("introduction".title().center(50)+'\n'+'-'*50)
	introduction = 'Hi Dear,\nI\'m Chapter 8.\nData Has to Go Somewhere.'
	print(introduction)
	c.function_end()

# [r/w/x/a][t/b]
# r means read.
# w means write. If the file doesn’t exist, it’s created. If the file does exist, it’s overwritten.
# x means write, but only if the file does not already exist. 
# a means append (write after the end) if the file exists. 
# t (or nothing) means text. 
# b means binary.

def test_write():
	print("write".title().center(50)+'\n'+'-'*50)
	poem = '''There was a young lady named Bright,
Whose speed was far faster than light;\nShe started one day\nIn a relative way,\nAnd returned on the previous night.\n''' 

	print(poem)
	len(poem) 
	
	# dir = main.py dir
	# 'module/textObj.txt'
	# '../textObj.txt'
	textObj = open('textObj.txt', 'wt')
	textObj.write(poem)
	textObj.close()

	fout = open('textObj', 'wt')
	print(poem, file=fout, sep='$', end='@')
	fout.close() 

	try:
		fout1 = open('relativity', 'xt')
		fout1.write('stomp stomp stomp')
		fout1.close()
	except FileExistsError:
		print('relativity already exists!. That was a close one.')
	c.function_end()


def special():
	print("special".title().center(50)+'\n'+'-'*50)

	c.function_end()
