FROM python:3.13-alpine AS build

# install UV
COPY --from=ghcr.io/astral-sh/uv:0.6.3 /uv /bin/uv

# copy files
COPY . /app/

WORKDIR /app
RUN uv sync --frozen

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "info"]
