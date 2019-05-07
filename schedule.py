from crontab import CronTab

cron = CronTab(user=True)
job = cron.new(command='bash /Users/username/Code/monitor/runmypythonscript.sh')
job.minute.every(1)

for item in cron:
    print(item)

cron.write()