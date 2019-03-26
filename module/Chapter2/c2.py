
def introduction():
	print("introduction".title().center(50)+'\n'+'-'*50)
	introduction = 'Hi Dear,\nI\'m Chapter 2.\nPy Ingredients: Numbers, Strings, and Variables.'
	print(introduction)
	function_end()


def test_operator():
	print("operator".title().center(50)+'\n'+'-'*50)
	print("integer (truncating) division: 7//2 =", 7//2)
	print("modulus (remainder): 7%3 =", 7%3)
	print("exponentiation3: 3**4 =", 3**4)
	print("divmod(9,5) =",divmod(9,5) )
	function_end()

def test_base():
	print("base".title().center(50)+'\n'+'-'*50)
	print("10 binary (base 2): 0b10 =", 0b10)
	print("10 Octal (base 10): 0o10 =", 0o10)
	print("10 Hexadecimal (base 16): 0x10 =", 0x10)
	function_end()

def test_str():
	print("string".title().center(50)+'\n'+'-'*50)
	print("Show \\t:")
	print('\tabc')
	print('a\tbc')
	print('ab\tc')

	print("print('a'+'b''):", 'a'+'b')
	print("print('a','b''):", 'a','b')

	print("'Na ' * 4 =", 'Na ' * 4)
	function_end()


def test_characters():
	print("character".title().center(50)+'\n'+'-'*50)
	letters = 'abcdefghijklmnopqrstuvwxyz'
	sample = [0,1,5,-1,-2,25]
	print("letters:", letters)
	for i in sample :
		print("letters["+str(i)+"] =", letters[i])

	print("\nSlice with [ start : end : step ] ")
	print("letters[:] =", letters[:])
	print("letters[20:] =", letters[20:])
	print("letters[10:] =", letters[10:])
	print("letters[12:15] =", letters[12:15])
	print("letters[-3:] =", letters[-3:])
	print("letters[18:-3] =", letters[18:-3])
	print("letters[-6:-2] =", letters[-6:-2])
	print("letters[-2:-6] =", letters[-2:-6])
	print("letters[::7] =", letters[::7])
	print("letters[4:20:3] =", letters[4:20:3])
	print("letters[-1::-1] =", letters[-1::-1])
	print("letters[::-1] =", letters[::-1])
	function_end()

def test_split_join():
	print("split and join".title().center(50)+'\n'+'-'*50)
	todos = 'get gloves,get mask,give cat vitamins,call ambulance'
	print("todos =", todos)
	print("todos.split(',') =", todos.split(','))

	crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
	print("\ncrypto_list =", crypto_list)
	print("' $ '.join(crypto_list) =", ' $ '.join(crypto_list))
	function_end()

def test_str_long():
	print("long string".title().center(50)+'\n'+'-'*50)
	poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.''' 
	print("poem:\n"+poem+'\n')
	print("poem[:13] =", poem[:13])
	print("len(poem) =", len(poem))
	print("poem.startswith('All'):", poem.startswith('All'))
	print("poem.endswith('That\'s all, folks!'):", poem.endswith('That\'s all, folks!'))
	print("poem.endswith('it die, no doubt.'):", poem.endswith('it die, no doubt.'))
	print("poem.find('the') =", poem.find('the'))
	print("poem.find('the',73) =", poem.find('the',73))
	print("poem.find('the',74) =", poem.find('the',74))
	print("poem.rfind('the') =", poem.rfind('the'))
	print("poem.count('the') =", poem.count('the'))
	print("\nalnum means only a-z & 0-9, no space and sign")
	print("poem.isalnum() =", poem.isalnum())
	print("'reqo331r.isalnum()' =", 'reqo331r'.isalnum())
	function_end()

def test_align():
	


def special():
	print("special".title().center(50)+'\n'+'-'*50)
	print("1. In Python 3, int can be any size, even greater than 64 bits.")
	function_end()

def function_end(): 
	print('-'*50+'\n')
