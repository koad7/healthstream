FROM python:3.10-slim as builder

WORKDIR /build

# Install system dependencies
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
       build-essential \
       procps

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM python:3.10-slim as production

WORKDIR /app

# Copy dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /build /app

