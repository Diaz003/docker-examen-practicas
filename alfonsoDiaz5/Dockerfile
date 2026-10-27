FROM python:3.12-alpine
WORKDIR /app_iot
COPY app5.py .
RUN pip install --upgrade pip
RUN pip install fastapi uvicorn
EXPOSE 7000
ENTRYPOINT ["uvicorn", "app5:app"]
CMD ["--host", "0.0.0.0", "--port", "7000"]
