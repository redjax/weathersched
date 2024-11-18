from weathersched.core import http_lib
from weathersched.weather_client.constants import WEATHERAPI_BASE_URL
from weathersched.weather_client.settings import WEATHERAPI_SETTINGS
from weathersched.weather_client.requests import return_current_weather_request,return_weather_forecast_request
from weathersched.weather_client.validators import validate_api_key

from loguru import logger as log
import httpx

_api_key: str = WEATHERAPI_SETTINGS.get("WEATHERAPI_API_KEY", default="")
_location: str = WEATHERAPI_SETTINGS.get("WEATHERAPI_LOCATION_NAME", default="london")
_aqi: bool = True

def _request_current_weather(api_key: str , location: str, include_aqi: bool) -> httpx.Response:
    req = return_current_weather_request(api_key=api_key, location=location, include_aqi=include_aqi)
    
    log.info(f"Requesting current weather for location: {location}")
    try:
        with http_lib.get_http_controller() as http_ctl:
            response = http_ctl.client.send(req)
            log.debug(f"Current weather response: [{response.status_code}: {response.reason_phrase}]")
            
            ## Raise an error for bad status codes
            response.raise_for_status()
            
            return response
        
    except httpx.RequestError as e:
        msg = f"({type(e)}) Unhandled exception requesting current weather for location '{location}'. Details: {e}"
        log.error(msg)
        
        raise
    

def get_current_weather(api_key: str =_api_key, location: str=_location, include_aqi: bool=_aqi):
    api_key = validate_api_key(api_key)
    
    try:
        current_weather_res = _request_current_weather(api_key=api_key, location=location, include_aqi=include_aqi)
        
        return current_weather_res
    except Exception as exc:
        msg = f"({type(exc)}) Unhandled exception requesting current weather. Details: {exc}"
        log.error(msg)
        
        raise exc