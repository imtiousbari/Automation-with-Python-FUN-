import time

def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def timer(seconds):
    interval = 5 * 60  # Interval of 5 minutes (5 * 60 seconds)
    elapsed_time = 0

    while seconds > 0:
        time_str = format_time(seconds)
        print(f"Time remaining: {time_str}")
        time.sleep(1)
        seconds -= 1
        elapsed_time += 1

        if elapsed_time % interval == 0:
            remaining_time = seconds
            print(f"Remaining time after {elapsed_time // 60} minutes: {format_time(remaining_time)}")

    print("Timer finished!")

# Set the duration of the timer (in seconds)
duration = 60 * 20

# Start the timer
timer(duration)
