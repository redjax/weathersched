# WeatherSched

A Python app to make scheduled weather requests.

## Notes

- On a fresh clone, do the following:
  - Install the environment with `uv run nox -s dev-env`
  - Copy settings files with `uv run nox -s fresh-clone-setup`
    - Make sure to edit the configuration files in [`config/`](./config)
  - Run `uv run nox -s init-db && uv run nox -s alembic-upgrade`
