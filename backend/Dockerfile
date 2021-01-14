### Build and install packages
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set workdir, install Python dependencies
WORKDIR /code/backend
COPY Pipfile Pipfile.lock /code/backend/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /code/backend/
EXPOSE 8000
