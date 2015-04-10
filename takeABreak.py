import time
import webbrowser


total_breaks = 1
break_count = 0

print("This program started on " + time.ctime())
while (break_count < total_breaks):
    time.sleep(25*60)
    webbrowser.open("https://www.youtube.com/watch?v=Pl6MCWMU8aE")
    break_count = break_count + 1
    print("This program ended on " + time.ctime())

