from machine import Pin, PWM
from time import sleep

# Button pin configuration
button_pin = Pin(11, Pin.IN, Pin.PULL_UP)

# PWM pin configuration
pwm_pin = Pin(19)
pwm = PWM(pwm_pin)

# Define the frequency values for the Mario sound notes
mario_notes  = {
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

# Flag to control sound playback
play_sound = False

def play_mario_sound():
    global play_sound
    mario_sound = ['E7', 'E7', '0', 'E7', '0', 'C7', 'E7', '0', 'G6', '0', '0', '0', 'G', '0', '0', '0',
                   'C7', '0', '0', 'G', '0', '0', 'E', '0', '0', 'A6', '0', 'B6', '0', 'A6', '0',
                   'G6', 'E6', '0', 'G6', 'A6', '0', 'F6', 'G6', '0', 'E6', '0', 'C6', 'D6', 'B6', '0',
                   '0', 'C7', '0', '0', 'G', '0', '0', 'E', '0', '0', 'A6', '0', 'B6', '0', 'A6', '0',
                   'G6', 'E6', '0', 'G6', 'A6', '0', 'F6', 'G6', '0', 'E6', '0', 'C6', 'D6', 'B6', '0',
                   '0']
    for note in mario_sound:
        if not play_sound:
            break

        if note == '0':
            pwm.duty_u16(0)  # No sound for this duration
        else:
            freq = mario_notes[note]
            pwm.freq(freq)
            pwm.duty_u16(32768)  
        sleep(0.1)

def stop_sound(pin):
    global play_sound
    play_sound = False
    pwm.duty_u16(0)

def restart_sound(pin):
    global play_sound
    play_sound = True

# Configure interrupt handlers for the button
button_pin.irq(trigger=Pin.IRQ_FALLING, handler=stop_sound)
restart_button_pin.irq(trigger=Pin.IRQ_FALLING, handler=restart_sound)

while True:
    if play_sound:
        play_mario_sound()
