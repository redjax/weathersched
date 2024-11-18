from dynaconf import Dynaconf

WEATHERAPI_SETTINGS = Dynaconf(environments=True, env="weatherapi", envvar_prefix="WEATHERAPI", settings_files=["settings.toml", ".secrets.toml"])