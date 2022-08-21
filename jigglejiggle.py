import sys
import time 
import pyautogui


JIGGLE_TIME_SECS_DEFAULT = 1 * 60.0 
JIGGLE_PIXELS_DEFAULT = 1

def main():
    JIGGLE_TIME_SECS = 0
    JIGGLE_PIXELS = 0

    try:
        JIGGLE_TIME_SECS = float(sys.argv[1])
    except:
        JIGGLE_TIME_SECS = JIGGLE_TIME_SECS_DEFAULT
        print(f"Using default jiggle time.")

    try:
        JIGGLE_PIXELS = int(sys.argv[2])
    except:
        JIGGLE_PIXELS = JIGGLE_PIXELS_DEFAULT

    print(f"Mouse will jiggle jiggle {JIGGLE_PIXELS} pixels every {f'{round(float(JIGGLE_TIME_SECS/60),1)} minutes' if JIGGLE_TIME_SECS>=60 else f'{JIGGLE_TIME_SECS} seconds'}")
        
    try:
        print('To exit, press Ctrl+C.')
        while True:
            pyautogui.move(JIGGLE_PIXELS,0)
            pyautogui.move(-JIGGLE_PIXELS,0)
            print(f"Jiggle Jiggle 👯 at ⌚ {time.strftime('%X %x')}")
            time.sleep(JIGGLE_TIME_SECS)
    except KeyboardInterrupt:
        print(f"\nYour mouse don't jiggle jiggle.\nNo more 😔")

if __name__=='__main__':
    main()