FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"
COPY "pyproject.toml" "uv.lock" ".python-version" ./
RUN uv sync --locked

COPY ingest_data2.py ingest_data2.py 

ENTRYPOINT ["python", "ingest_data2.py"]