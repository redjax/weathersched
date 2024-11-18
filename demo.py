from huey import SqliteHuey, crontab

import httpx
from weathersched.core import http_lib
from weathersched.core import setup
from weathersched.core.settings import LOGGING_SETTINGS
from weathersched import weather_client
from loguru import logger as log
import logging

from weathersched.huey_app.config import huey
from weathersched.huey_app.tasks import add, scheduled_current_weather, get_current_weather


if __name__ == "__main__":
    setup.setup_logging(log_level=LOGGING_SETTINGS.get("LOG_LEVEL", default="INFO"), enable_loggers=["weathersched", "huey.consumer"], colorize=True, add_error_file_logger=True, add_file_logger=True)
    
    result = add(1,2)
    print(f"1 + 2 = {result.get(blocking=True)}")
    
    current_weather = get_current_weather()
    print(f"Current weather: {current_weather.get(blocking=True)}")