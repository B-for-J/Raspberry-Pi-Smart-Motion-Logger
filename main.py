import time
from motion import setup, motion_detected, cleanup
from logger import log_motion

def main():
    print("Starting Motion Logger...")
    setup()

    try:
        while True:
            if motion_detected():
                log_motion()
                print("Motion detected!")
                time.sleep(5)  # debounce
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Stopping program.")
    finally:
        cleanup()

if __name__ == "__main__":
    main()
