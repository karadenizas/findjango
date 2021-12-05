from apscheduler.schedulers.background import BackgroundScheduler
from investment.task_result import target_date_job
from pytz import utc

# European Central Bank refresh date 16:00 CET. converted to GMT time is 15:00. 5 minutes delayed because may be server will busy.
def start():
    scheduler = BackgroundScheduler(timezone=utc)
    scheduler.add_job(target_date_job, 'cron', hour=15, minute=5)
    scheduler.start()