
import os

FILE_NAME = 'userinfo.txt'

if not os.path.exists(FILE_NAME):
	filename = open(FILE_NAME, 'w')
	filename.close()

##########################################################################################################

def createUserFileInfo(password, question, answer):
	filename = open(FILE_NAME, 'a')
	filename.write(username + "\n")
	filename.write(password + "\n")
	filename.write(question + "\n")
	filename.write(answer + "\n")
	filename.close()

def getLines():
	filename = open('userinfo.txt', 'r')
	lines = filename.readlines()
	filename.close()
	return lines

def changePassword():
	print('This is your question [' + getLines()[2].strip() + ']')
	answer = input('What is your answer? ')
	if answer == getLines()[3].strip():
		return 'Your password is: ' + getLines()[1].strip()
	return 'erorr, goodbye!'


##########################################################################################################

username = input('username: ')
password = input('password: ')

if os.stat(FILE_NAME).st_size == 0:
	question = input('question: ')
	answer   = input('answer: ')
	createUserFileInfo(password, question, answer)

elif getLines()[0].strip() == username and getLines()[1].strip() == password:
	print('Welcome ' + username)
else:
	print('username or password error')
	forget = input('forget your password? y/n ')
	if forget == 'y':
		print(changePassword())
