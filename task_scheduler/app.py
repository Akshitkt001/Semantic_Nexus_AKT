import schedule
import time

def job():
    print("Executing scheduled task...")

# Schedule the job every minute
schedule.every(1).minutes.do(job)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
