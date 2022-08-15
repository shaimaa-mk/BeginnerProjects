import time
import datetime
#
# print("This is the start of the program")
# seconds = time.time()
# print(f"Time in seconds since epoch: {seconds}")
# local = time.ctime()
# print(f"Local time: {local}")
# time.sleep(5)
# print("This prints after 5 seconds later.")
#
# current = datetime.datetime.now()
# print(f"Current Date: {str(current)}")
# one_year = current + datetime.timedelta(days=365)
# print(f"The date in year: {str(one_year)}")
# Timer starts
starttime = time.time()
lasttime = starttime
lapnum = 1
value = " "

print("Press ENTER for each lap.\nType Q and press ENTER to stop.")

while value.lower() != 'q':
    # Input for the Enter key press
    value = input()
    # The current lap-time
    laptime = round((time.time() - lasttime), 2)
    # Ttoal time elapsed since the timer started
    totaltime = round((time.time() - starttime), 2)
    # Printing the lapnum, laptime and total ti
    # me
    print(f"Lap No. : {str(lapnum)}")
    print(f"Lap time : {str(laptime)}")
    print(f"Total time : {str(totaltime)}")

    print("*"*20)

    # Update the previous total time and lapnum
    lasttime = time.time()
    lapnum += 1
print("Exercise complete!")

