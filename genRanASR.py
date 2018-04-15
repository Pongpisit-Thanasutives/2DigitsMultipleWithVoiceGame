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
corr = 0
gameStatus = False

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
			gameStatus = True
			break
	if gameStatus:break

	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
	
	r = sr.Recognizer()
	with sr.Microphone() as source:
  		audio = r.listen(source)

	try:
		answer = (a * 10 + b) * (c * 10 + d)
		ans = r.recognize_google(audio,language = "th-TH")
		print()
		print("You answered " + ans)
		
		try:
			if int(ans.replace(' ', '').replace('Fun', '1')) == answer:
				print('Your answer is correct!')
				corr += 1
			else:
				print('Your answer is incorrect TT')
		except:
			pass
	except:
		print("Could not understand audio")
		print("Please check the answer yourself")		

	process_times.append(time.time() - start_time)
	print('answer =', answer)
	print('--' * 10)

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)

print()
print('Time used', (time.time() - start_time) // 60 ,'minutes', round((time.time() - start_time) % 60, 2), 'seconds')
print('You scored', corr, 'out of', len(process_times), 'problems')
if len(process_times) > 0:
	print('Average time per problem =', round(sum(process_times) / len(process_times),2), 'seconds')
