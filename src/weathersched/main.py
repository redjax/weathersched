import logging

log = logging.getLogger(__name__)

from weathersched.core import setup, db, http_lib
from weathersched.core.setup import LOGGING_SETTINGS
from weathersched.domain import weather, location
from weathersched.remote_apis import weatherapi_client


def main():
    log.info("Start weathersched")

    log.debug(f"DB settings: {db.settings.DB_SETTINGS.as_dict()}")
    current_weather = weatherapi_client.client.get_current_weather()
    log.info(f"Current weather: {current_weather}")

    weather_forecast = weatherapi_client.client.get_weather_forecast()
    log.info(f"Weather forecast: {weather_forecast}")


if __name__ == "__main__":
    setup.setup_logging(level=LOGGING_SETTINGS.get("LOG_LEVEL", default="INFO"))
    setup.setup_database()

    main()
