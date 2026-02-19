import time
import sys

def run_timer(seconds):
    """Counts down from the given number of seconds."""
    while seconds > 0:
        # divmod calculates minutes and remaining seconds
        mins, secs = divmod(seconds, 60)
        # \r and end="" allow the timer to stay on one line
        print(f"Time remaining: {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    
    print("\nTime's up! 🔔")

def main():
    while True:
        choice = input("\nChoose (25) Work, (5) Break, or (e) Exit: ").lower()
        
        if choice == "25":
            print("Focus session started...")
            run_timer(25 * 60) # 1500 seconds
        elif choice == "5":
            print("Break session started...")
            run_timer(5 * 60)  # 300 seconds
        elif choice == "e":
            print("Great work today! Goodbye.")
            break
        else:
            print("Invalid input. Please type 25, 5, or e.")

if __name__ == "__main__":
    main()