import time
import datetime


# Declare countdown function
def countdown(h, m, s):
    # Calculate the total number of seconds
    totalseconds = h * 3600 + m * 60 + s

    # While loop that checks if total seconds reach zero
    # If not zero, decrement total seconds by one second
    while totalseconds > 0:
        # Timer represent time left on countdown
        timer = datetime.timedelta(seconds=totalseconds)

        # Print the time left on the timer
        print(timer)
        # print(timer, sep="\r", flush=True)
        # Delay the program one second
        time.sleep(1)

        # Reduce total time by one second
        totalseconds -= 1

    print("Bzzzt! The countdown is at a zero second.")


# Inputs for hours, minutes, seconds in timer
h = input("Enter the time in hour:")
m = input("Enter the time in minutes:")
s = input("Enter the time in seconds:")

# call countdown function
countdown(int(h), int(m), int(s))
