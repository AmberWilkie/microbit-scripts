from microbit import *

while True:
    fuck_off = button_a.was_pressed()
    while fuck_off:
        display.scroll('FUCK OFF')
        if button_b.was_pressed():
            break

display.clear()