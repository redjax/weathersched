from huey import SqliteHuey

from weathersched.core.setup import setup_logging
from weathersched.core.settings import LOGGING_SETTINGS

if __name__ == "__main__":
    setup_logging(log_level=LOGGING_SETTINGS.get("LOG_LEVEL", default="INFO"), enable_loggers=["weathersched", "huey.consumer"], colorize=True, add_error_file_logger=True, add_file_logger=True)

# Initialize Huey with SQLite backend
huey = SqliteHuey(filename='huey.db')