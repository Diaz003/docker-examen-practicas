FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt app8.py .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python","app8.py"]
