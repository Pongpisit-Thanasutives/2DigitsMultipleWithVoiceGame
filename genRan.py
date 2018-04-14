import time
import tty
import sys
import termios
from sys import exit
from random import randint

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

	process_times.append(time().time() - start_time)
	print('answer =', (a * 10 + b) * (c * 10 + d))
	print('--' * 10)
	
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)