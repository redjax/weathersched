from huey import crontab, CancelExecution
from .config import huey

from weathersched import weather_client

from loguru import logger as log

@huey.task()
def add(a, b):
    return a + b

@huey.periodic_task(crontab(minute="*/1"), retries=3, retry_delay=10, expires=45)
def say_hello_each_minute():
    print("Hello, from Huey! I do this every minute...")
    return

@huey.periodic_task(crontab(minute="*/10"), retries=3, retry_delay=60, expires=60*5)
def scheduled_current_weather():
    try:
        current_weather = weather_client.current_weather.get_current_weather()
        
        print(f"Current weather: {current_weather}")
        
        return current_weather.json()
    except Exception as exc:
        msg = f"({type(exc)}) Unhandled exception requesting current weather. Details: {exc}"
        log.error(msg)
        
        raise CancelExecution(retry=True)
    
@huey.task()
def get_current_weather():
    try:
        scheduled_current_weather()
    except Exception as exc:
        msg = f"({type(exc)}) Unhandled exception requesting current weather. Details: {exc}"
        log.error(msg)
        
        raise CancelExecution(retry=True)