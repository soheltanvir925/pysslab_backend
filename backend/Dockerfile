FROM python:3.13.5-slim

# Set working directory
WORKDIR /app

# Install Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Django project
COPY . .
# Copy entrypoint script
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Prevents python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1
# Use entrypoint script
ENTRYPOINT ["./entrypoint.sh"]

