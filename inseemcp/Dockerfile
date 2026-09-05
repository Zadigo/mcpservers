FROM python:3.12-slim-trixie AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

ADD https://astral.sh/uv/0.12.10/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

ENV PATH="/root/.local/bin/:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

# Copy dependency files FIRST for caching, before installing
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project --no-dev

RUN addgroup -S django && adduser -S django -G django

COPY . .

EXPOSE 8000
ENTRYPOINT ["uv", "fastmcp", "run", "--host", "0.0.0.0", "--port", "8000", "--project", "app"]
