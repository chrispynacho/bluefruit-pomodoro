import time
from adafruit_circuitplayground import cp

# CircuitPlayground Bluefruit as a pomodoro counter
# probably works on a regular CircuitPlayground too

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
cp.pixels.brightness = 0.1
cp.pixels.auto_write = True

MODE_A = 1
MODE_B = 2
mode = MODE_A

MODE_COLORS = {
    MODE_A: GREEN,
    MODE_B: BLUE
}
MODE_DURATION = {
    MODE_A: 1500,  # 25 minutes
    MODE_B: 300    # 5 minutes
}

STATE_PAUSED = 1
STATE_COUNTING = 2
state = STATE_PAUSED

counter = 0


# handle pixel colors
def draw():
    color = MODE_COLORS[mode]
    limit = MODE_DURATION[mode]

    # draw count down timer if counter hasn't reached limit, otherwise blink
    if counter < limit:
        numPixelsOn = cp.pixels.n * counter // limit

        for p in range(cp.pixels.n):
            if p > numPixelsOn - 1:
                cp.pixels[p] = color
            else:
                cp.pixels[p] = BLACK
    else:
        # blink mode - blink all pixels red every other second
        now = int(time.monotonic())
        if now % 2:
            color = RED
            doBeep = True
        else:
            doBeep = False
        for p in range(cp.pixels.n):
            cp.pixels[p] = color

        # beep in time with the blink for the first 5 seconds
        if doBeep and counter < limit + 5:
            cp.start_tone(600)
        else:
            cp.stop_tone()


# Beep n times - blocking
def beep(n=3):
    for _ in range(n):
        cp.start_tone(440)
        time.sleep(0.2)
        cp.stop_tone()
        time.sleep(0.1)


# Event loop
prev = 0
now = 0
while True:
    prev = now
    now = time.monotonic()
    # Get input
    if cp.button_a:
        mode = MODE_A
        beep()
        counter = 0
    if cp.button_b:
        mode = MODE_B
        beep()
        counter = 0

    # Update state
    isCounting = cp.switch
    if isCounting:
        counter += now - prev
        print(f"counter: {counter}")

    # Render
    draw()

    # Small sleep
    time.sleep(0.25)
