from crontab import CronTab

my_cron = CronTab(user="Avnish")
# job = my_cron.new(
# command='python /Users/avnish/Documents/Programming/queue-python/cron-job.py')
# job.minute.every(1)
my_cron.remove_all()
my_cron.write()
