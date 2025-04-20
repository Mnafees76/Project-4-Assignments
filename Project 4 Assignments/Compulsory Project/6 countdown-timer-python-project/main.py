import time  # Importing time module to use the sleep function

def countdown_timer(seconds):
    """
    Function to run a countdown timer.
    :param seconds: Total seconds for countdown
    """
    while seconds > 0:
        # Convert total seconds into minutes and seconds
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)  # Format time as MM:SS
        
        # Print the formatted time and overwrite previous output
        print(time_format, end='\r')  
        time.sleep(1)  # Pause for 1 second
        seconds -= 1  # Decrease time by 1 second
    
    print("00:00\nTime's up!")  # Display message when countdown ends

# Take user input for countdown duration in seconds
total_seconds = int(input("Enter time in seconds for countdown: "))  
countdown_timer(total_seconds)  # Start the countdown timer
