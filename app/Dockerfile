FROM python:slim-buster

# Create a non-root user and group
RUN groupadd -r app && useradd -r -g app app

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app/

# Adjust permissions to allow the 'app' user to write into the /app/ directory
RUN chown -R app:app /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Switch to the 'app' user
USER app

# Start the application
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--log-level", "info"]


