FROM python:3.11-slim AS base
## Install UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

## Set ENV variables to control Python/pip behavior inside container
ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1 \
    ## Pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

FROM base AS build

## Tell Dynaconf to always load from the environment first while in the container
ENV DYNACONF_ALWAYS_LOAD_ENV_VARS=True

WORKDIR /project

COPY pyproject.toml .
COPY uv.lock .
COPY README.md .

COPY ./scripts ./scripts

FROM build AS stage

WORKDIR /project

COPY ./src ./src
COPY ./migrations ./migrations
COPY ./alembic.ini ./alembic.ini

RUN uv sync --all-extras --dev
RUN uv pip install .

FROM stage AS runtime

COPY --from=build /project /project
WORKDIR /project

ENTRYPOINT ["uv", "run", "scripts/db_init.py", "&&", "uv", "run", "alembic", "upgrade", "head"]
