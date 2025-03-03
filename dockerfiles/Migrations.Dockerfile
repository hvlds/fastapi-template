FROM python:3.13-alpine AS build

# install UV
COPY --from=ghcr.io/astral-sh/uv:0.6.3 /uv /bin/uv

# copy files
COPY . /app/

WORKDIR /app
RUN uv sync --frozen --group migrations

CMD ["uv", "run", "alembic", "upgrade", "head"]
