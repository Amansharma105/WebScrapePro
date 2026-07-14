from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

def check_prices():
    print("Checking product prices...")

scheduler.add_job(check_prices, "interval", hours=1)
