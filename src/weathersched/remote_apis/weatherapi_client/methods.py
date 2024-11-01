from __future__ import annotations

import logging

log = logging.getLogger(__name__)

from weathersched.core import http_lib, setup

from .settings import WEATHERAPI_SETTINGS, weatherapi_settings

def get_current_weather(
    location: str = weatherapi_settings.location,
    api_key: str = weatherapi_settings.api_key,
):
    http_ctl = http_lib.get_http_controller()

    params = {"key": api_key, "q": location, "aqi": "yes"}

    req = http_lib.build_request(
        url="https://api.weatherapi.com/v1/current.json", params=params
    )

    with http_ctl as http:
        res = http.client.send(req)

    log.info(f"Current weather response: [{res.status_code}: {res.reason_phrase}]")

    log.debug(f"Response content: {res.text}")

    return res
