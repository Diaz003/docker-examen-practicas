FROM python:3.11-alpine
WORKDIR /app_erp
COPY app6.py .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir flask
EXPOSE 6000
CMD ["python", "app6.py"]
