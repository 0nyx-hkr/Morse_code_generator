import time
import pyaudio
import numpy as np

class Morse:
    MORSE_CODE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }

    def __init__(self, letter):
        self.letter = letter.upper()
        self.volume = 0.5
        self.fs = 44100
        self.duration_dot = 0.439
        self.duration_dash = self.duration_dot * 3
        self.f = 440.0
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paFloat32, channels=1, rate=self.fs, output=True)

    def play_sound(self, duration):
        samples = (np.sin(2*np.pi*np.arange(self.fs*duration)*self.f/self.fs)).astype(np.float32)
        self.stream.write(self.volume * samples)

    def play_morse_code(self, code):
        for symbol in code:
            if symbol == '.':
                self.play_sound(self.duration_dot)
            elif symbol == '-':
                self.play_sound(self.duration_dash)
            time.sleep(self.duration_dot)  # Pause between symbols

    def morse_code(self):
        for letter in self.letter:
            if letter in Morse.MORSE_CODE:
                code = Morse.MORSE_CODE[letter]
                self.play_morse_code(code)
                time.sleep(2)  # Pause between letters

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

if __name__ == "__main__":
    string = input("Enter string: ")
    morse_obj = Morse(string)
    morse_obj.morse_code()
    morse_obj.close()
