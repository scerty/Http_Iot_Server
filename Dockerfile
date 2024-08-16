# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Create a virtual environment


# Activate the virtual environment


# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /code/

# Ensure manage.py and other project files are not overwritten
RUN if [ ! -f /code/manage.py ]; then django-admin startproject myproject .; fi

# Expose port 8000 and run the development server
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
