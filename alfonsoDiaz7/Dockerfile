FROM python:3.10-slim
WORKDIR /usr/src/app
COPY requirements.txt app7.py .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python","app7.py"]
