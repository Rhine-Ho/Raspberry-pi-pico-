from machine import Pin, PWM
from time import sleep

button = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_UP)

pwm = PWM(Pin(19))  

# Define the frequency values for the Mario sound notes
mario_notes = {
    'E7': 2637,
    'E': 3136,
    'C7': 2093,
    'D7': 2349,
    'G6': 1568,
    'G': 3136,
    'E6': 1318,
    'A6': 1760,
    'B6': 1976,
    'A': 440,
    'A#': 466,
    'C': 523,
    'C#': 554,
    'D': 587,
    'D#': 622,
    'F': 698,
    'F#': 740,
    'G': 784,
    'G#': 830
}

def play_mario_sound():
    # Mario sound notes in order
    mario_sound = ['E7', 'E7', '0', 'E7', '0', 'C7', 'E7', '0', 'G6', '0', '0', '0', 'G', '0', '0', '0',
                   'C7', '0', '0', 'G', '0', '0', 'E', '0', '0', 'A6', '0', 'B6', '0', 'A6', '0',
                   'G6', 'E6', '0', 'G6', 'A6', '0', 'F6', 'G6', '0', 'E6', '0', 'C6', 'D6', 'B6', '0',
                   '0', 'C7', '0', '0', 'G', '0', '0', 'E', '0', '0', 'A6', '0', 'B6', '0', 'A6', '0',
                   'G6', 'E6', '0', 'G6', 'A6', '0', 'F6', 'G6', '0', 'E6', '0', 'C6', 'D6', 'B6', '0',
                   '0']

    for note in mario_sound:
        if note == '0':
            pwm.duty_u16(0)  # No sound for this duration
        else:
            freq = mario_notes[note]
            pwm.freq(freq)
            pwm.duty_u16(16384)  # 50% duty cycle
        sleep(0.1)


while True:
        play_mario_sound()


