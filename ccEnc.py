import string

LETTERS = string.ascii_lowercase

mod = 'e'
key = 3
msg = input('Enter your message: ')

def encrypt(key, mod):
	global key
	encryptedMsg = ''

	for letter in msg:
		shift = LETTERS.find(letter) + key
		if shift > 25:
			shift = key

		if shift != 2:
			encryptedMsg += LETTERS[shift]
		else:
			encryptedMsg += letter
		
	print(encryptedMsg)
		
encrypt(key, mod)
