FROM python:3.10-slim
WORKDIR /app_sales 
COPY requirements.txt app9.py .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 7000
CMD ["uvicorn","app9:app","--host","0.0.0.0","--port","7000"]
