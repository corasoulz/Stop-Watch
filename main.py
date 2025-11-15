import datetime
import time

print("Press Enter to start...")
input()

start_time = datetime.datetime.now()

print("Stopwatch running! (Press Ctrl + C to stop)\n")

try:
    while True:
        now = datetime.datetime.now()
        diff = now - start_time
        total_seconds = int(diff.total_seconds())

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}", end="\r")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopped!")
