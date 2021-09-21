from pyo import *


def play_key(key):
    s = Server().boot()

    if key == "C":
        s.start()
        k = Sine(261.63, 0, 0.1).out()
    elif key == "D":
        k = Sine(293.66, 0, 0.1).out()
        s.start()
    elif key == "E":
        k = Sine(329.63, 0, 0.1).out()
    elif key == "F":
        k = Sine(349.23, 0, 0.1).out()
    elif key == "G":
        k = Sine(392.00, 0, 0.1).out()
    elif key == "A":
        k = Sine(440.00, 0, 0.1).out()
    elif key == "B":
        k = Sine(493.88, 0, 0.1).out()
    elif key == "C#":
        k = Sine(277.18, 0, 0.1).out()
    elif key == "D#":
        k = Sine(311.13, 0, 0.1).out()
    elif key == "F#":
        k = Sine(369.99, 0, 0.1).out()
    elif key == "G#":
        k = Sine(415.30, 0, 0.1).out()
    else:
        k = Sine(466.16, 0, 0.1).out()

    return k
