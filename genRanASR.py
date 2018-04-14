import time
import tty
import sys
import termios
from sys import exit
from random import randint
import speech_recognition as sr

r = sr.Recognizer()
orig_settings = termios.tcgetattr(sys.stdin)
print('Start the game !')
print()
process_times = []
start_time = time.time()

while True:

	a = randint(1, 9)
	b = randint(0, 9)
	c = randint(1, 9)
	d = randint(0, 9)

	show_first = str(a) + str(b)
	show_second = str(c) + str(d)

	print(show_first)
	print('    X')
	print(show_second)

	start_time_pb = time.time()
	
	tty.setraw(sys.stdin)
	x = 0
	while x != chr(32):
		x=sys.stdin.read(1)[0]
		if x == chr(27):
			print()
			print('Time used', (time.time() - start_time) // 60 ,'minutes', round((time.time() - start_time) % 60, 1), 'seconds')
			print('You played', len(process_times), 'problems')
			if len(process_times) > 0:
				print('Average time per problem =', sum(process_times) / len(process_times), 'seconds')
			exit(0)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
	
	r = sr.Recognizer()
	with sr.Microphone() as source:
  		audio = r.listen(source)
  	
  	try:
  		ans = r.recognize_google(audio,language = "th-TH")
  		print("You said " + ans)
  	except sr.RequestError as e:
  		print("Could not understand audio")

	process_times.append(time().time() - start_time)
	answer = (a * 10 + b) * (c * 10 + d)
	print('answer =', answer)
	print('--' * 10)

	if int(ans.replace(' ', '')) == answer:
		print('Your answer is correct!')
	else:
		print('Your answer is incorrect or I cannot recognize your voice TT')
	
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)