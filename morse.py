import time
import pyaudio
import numpy as np
import time

p = pyaudio.PyAudio()

class Morse:
	def __init__(self,letter):
		self.letter = letter
		def dot():
			volume = 0.5     # range [0.0, 1.0]
			fs = 44100       # sampling rate, Hz, must be integer
			duration = 0.439   # in seconds, may be float
			f = 440.0        # sine frequency, Hz, may be float

			# generate samples, note conversion to float32 array
			samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

			# for paFloat32 sample values must be in range [-1.0, 1.0]
			stream = p.open(format=pyaudio.paFloat32,
							channels=1,
							rate=fs,
							output=True)

			# play. May repeat with delifferent volume values (elif done interactively) 
			stream.write(volume*samples)
			stream.stop_stream()
		def dash():
			volume = 0.5     # range [0.0, 1.0]
			fs = 44100       # sampling rate, Hz, must be integer
			duration = 0.439*2.0   # in seconds, may be float
			f = 440.0        # sine frequency, Hz, may be float

			# generate samples, note conversion to float32 array
			samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

			# for paFloat32 sample values must be in range [-1.0, 1.0]
			stream1 = p.open(format=pyaudio.paFloat32,
							channels=1,
							rate=fs,
							output=True)


			stream1.write(volume*samples)
			stream1.stop_stream()
		for i in letter:
			if i == 'a' or i == 'A':
					dot();dash();time.sleep(1)
			elif i == 'b'or i == 'B':
					dash();dot();dot();dot();time.sleep(1)
			elif i == 'c'or i == 'C':
					dash();dot();dash();dot();time.sleep(1)
			elif i == 'd'or i == 'D':
					dash();dot();dot();time.sleep(1)		
			elif i == 'e'or i == 'E':
					dot();time.sleep(1)
			elif i == 'f'or i == 'F':
					dot();dot();dash();dot();time.sleep(1)
			elif i == 'g'or i == 'G':
					dash();dash();dot();time.sleep(1)
			elif i == 'h'or i == 'H':
					dot();dot();dot();dot();time.sleep(1)
			elif i == 'i'or i == 'I':
					dot();dot();time.sleep(1)
			elif i == 'j'or i == 'J':
					dot();dash();dash();dash();time.sleep(1)
			elif i == 'k'or i == 'K':	
					dash();dot();dash();time.sleep(1)
			elif i == 'l'or i == 'L':
					dot()
					dash()
					dot()
					dot()
					time.sleep(1)
			elif i == 'm'or i == 'M':
					dash()
					dash()
					time.sleep(1)
			elif i == 'n'or i == 'N':
					dash() 
					dot()
					time.sleep(1)
			elif i == 'o'or i == 'O':
					dash()
					dash()
					dash()
					time.sleep(1)
			elif i == 'p'or i == 'P':
					dot()
					dash()
					dash()
					dot()
					time.sleep(1)
			elif i == 'q'or i == 'Q':
					dash()
					dash()
					dot()
					dash()
					time.sleep(1)
			elif i == 'r'or i == 'R':
					dot()
					dash()
					dot()
					time.sleep(1)
			elif i == 's'or i == 'S':
					dot()
					dot()
					dot()
					time.sleep(1)
			elif i == 't'or i == 'T':
					dash()
					time.sleep(1)
			elif i == 'u'or i == 'U':
					dot()
					dot()
					dash()
					time.sleep(1)
			elif i == 'v'or i == 'V':
					dot()
					dot()
					dot()
					dash()
					time.sleep(1)	
			elif i == 'w'or i == 'W':
					dot()
					dash()
					dash()
					time.sleep(1)
			elif i == 'x'or i == 'X':
					dash()
					dot()
					dot()
					dash()
					time.sleep(1)
			elif i == 'y'or i == 'Y':
					dash()
					dot()
					dash()
					dash()
					time.sleep(1)
			elif i == 'z'or i == 'Z':
					dash()
					dash()
					dot()
					dot()
					time.sleep(1)
			elif i == '0':
					dash()
					dash()
					dash()
					dash()
					dash()
					time.sleep(1)
			elif i == '9':
					dash()
					dash()
					dash()
					dash()
					dot()
					time.sleep(1)
			elif i == '8':
					dash()
					dash()
					dash()
					dot()
					dot()
					time.sleep(1)
			elif i == '7':
					dash()
					dash()
					dot()
					dot()
					dot()
					time.sleep(1)
			elif i == '6':
					dash()
					dot()
					dot()
					dot()
					dot()
					time.sleep(1)
			elif i == '5':
					dot()
					dot()
					dot()
					dot()
					dot()
					time.sleep(1)
			elif i == '4':
					dot()
					dot()
					dot()
					dot()
					dash()
					time.sleep(1)
			elif i == '3':
					dot()
					dot()
					dot()
					dash()
					dash()
					time.sleep(1)
			elif i == '2':
					dot()
					dot()
					dash()
					dash()
					dash()
					time.sleep(1)
			elif i == '1':
					dot()
					dash()
					dash()
					dash()
					dash()
					time.sleep(1)
			else:
				 continue			
string = input("Enter string:")
Morse(string)
