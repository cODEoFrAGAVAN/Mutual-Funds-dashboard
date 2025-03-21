# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /MF

# Copy the project files to the container
COPY . /MF/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Gunicorn will run on
EXPOSE 8000

# Run migrations and collect static files
# RUN python manage.py makemigrations
# RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput

# Start Gunicorn server
CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:8000", "mf.wsgi:application"]
