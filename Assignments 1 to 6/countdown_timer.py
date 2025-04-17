import time

def start_timer(duration):
    for remaining in range(duration, -1, -1):
        minutes = divmod(remaining, 60)[0]
        seconds = divmod(remaining, 60)[1]
        print(f"Remaining Time -> {minutes:02d} min : {seconds:02d} sec", end="\r")
        time.sleep(1)
    
    print("\nCountdown complete!")

try:
    total_seconds = int(input("Set countdown duration (in seconds): "))
    start_timer(total_seconds)
except ValueError:
    print("Invalid input! Please enter a number.")
