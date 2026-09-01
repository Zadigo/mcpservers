import huey
from huey import crontab

huey_app = huey.RedisHuey('frelectedofficials')

@huey_app.periodic_task(crontab(day='*/14')) # Run every 14 days
def api_watcher():
    # This function will be called by the Huey worker to watch for API changes
    # You can implement your logic here to check for changes in the API
    # For example, you can make an HTTP request to the API and check for updates
    pass
