# bluefruit-pomodoro
I wanted a simple pomodoro timer that was not on my screen with an alert that would get my attention without being annoying.
I got this working on an [Adafruit Circuit Playground Bluefruit](https://learn.adafruit.com/adafruit-circuit-playground-bluefruit). This would probably work on a [Circuit Playground](https://learn.adafruit.com/introducing-circuit-playground) or [Circuit Playground Express](https://learn.adafruit.com/category/express) but I don't have one of those to test with.

# Install
- Connect the Circuit Playground Bluefruit to your computer via USB.
- Follow instructions for [Installing CircuitPython on Circuit Playground Bluefruit](https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/circuit-playground-bluefruit-circuitpython-libraries#installing-circuitpython-libraries-on-circuit-playground-bluefruit-3048343-2).
- Copy the code.py file onto the Circuit Playground Bluefruit. On a Mac you will probably need to run `cp code.py /Volumes/code.py` but make sure you do whatever method works for your device and OS.

# Instruction Manual
- The slide switch pauses the count down in the right position and continues the countdown in the left position
- Press button A to start counting down 25 minutes.
- The neopizels will light up green, with one going out every 2m 30s
- At the end of 25 minutes all of the neopixels will turn off and the piezo buzzer will beep 3 times. Then the neopizels will blink red and green indefinitely.
- Press button B to start counting down 5 minutes.
- The neopizels will light up blue, with one going out every 30s
- At the end of 5 minutes all of the neopixels will turn off and the piezo buzzer will beep 3 times. Then the neopizels will blink red and blue indefinitely.
- There is no off switch on the bluefruit, so just unplug it from USB and/or battery.