# Use a base image with Python and the necessary dependencies 
FROM python:3.11-slim 
WORKDIR /app 
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt 
COPY . . 
CMD ["python", "your_app.py"] 
