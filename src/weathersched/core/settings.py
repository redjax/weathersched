from dynaconf import Dynaconf

LOGGING_SETTINGS = Dynaconf(
    environments=True,
    env="logging",
    envvar_prefix="LOG",
    settings_files=["settings.toml", ".secrets.toml"],
)
