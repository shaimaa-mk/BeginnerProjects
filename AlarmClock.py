import os
import datetime
import random
import webbrowser
# If video text file does not exist, create one
import time

if not os.path.isfile("youtube_alarm_videos.txt"):
    print("Creating youtube_alarm_videos.txt file ....")
    with open("youtube_alarm_videos.txt", "w") as alarm_file:
        alarm_file.write("https://www.youtube.com/watch?v=goPatm4dyzA")


def check_alarm_input(alarm_time):
    """"checks to see if the user has entered a valid alarm time"""
    if len(alarm_time) == 1:
        if alarm_time[0] < 24 and alarm_file[0] > 0:
            return True
    elif len(alarm_time) == 2:
        if alarm_time[0] < 24 and alarm_time[0] > 0 and \
                alarm_time[1] < 60 and alarm_time[1] > 0:
            return True
    elif len(alarm_time) == 3:
        if alarm_time[0] < 24 and alarm_time[0] > 0 and \
           alarm_time[1] < 60 and alarm_time[1] > 0 and\
           alarm_time[2] < 60 and alarm_time[2] > 0:
            return True


# Get user input for alarm time
print("Set alarm time")
while True:
    alarm_input = input(">> ")
    try:
        alarm_time = [int(i) for i in alarm_input.split(":")]
        if check_alarm_input(alarm_time):
            break
        else:
            raise ValueError
    except ValueError:
        print("Enter a time : HH:MM:SS or HH:MM .")


# Convert alarm time to seconds
seconds_hms = [3600, 60, 1]
alarm_seconds = sum([a*b for a, b in zip(seconds_hms[:len(alarm_time)], alarm_time)])


# Get the current time of day in seconds
now = datetime.datetime.now()
current_time_seconds = sum([a*b for a, b in zip(seconds_hms, [now.hour, now.minute, now.second])])


# Calculate difference between alarm time and current time
time_diff_seconds = alarm_seconds - current_time_seconds

if time_diff_seconds < 0:
    time_diff_seconds += 86400  # number of seconds of a day

# Display the time amount until alarm goes off
print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))

# Sleep until alarm goes off
time.sleep(time_diff_seconds)


# Time to alarm set of
print("Wake Up!")


with open("youtube_alarm_videos.txt", "r") as alarm_file:
    videos = alarm_file.readlines()

# Open a random video from the list
webbrowser.open(random.choice(videos))
