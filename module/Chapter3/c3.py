def introduction():
	print("introduction".title().center(50)+'\n'+'-'*50)
	introduction = 'Hi Dear,\nI\'m Chapter 3.\nPy Filling: Lists, Tuples, Dictionaries, and Sets.'
	print(introduction)
	function_end()

def test_convert_to_list():
	list('cat') 

	a_tuple = ('ready', 'fire', 'aim') 
	list(a_tuple) 

	birthday = '1/6/1952' 
	birthday.split('/') 
	splitme = 'a/b//c/d///e' 
	splitme.split('/') 
	splitme = 'a/b//c/d///e' 
	splitme.split('//') 

def test_get_item():
	marxes = ['Groucho', 'Chico', 'Harpo'] 
	print("marxes[0]", marxes[0])
	print("marxes[1]", marxes[1])
	print("marxes[2]", marxes[2])
	print("marxes[-1]", marxes[-1])
	print("marxes[-2]", marxes[-2])
	print("marxes[-3]", marxes[-3])



















def function_end(): 
	print('-'*50+'\n')