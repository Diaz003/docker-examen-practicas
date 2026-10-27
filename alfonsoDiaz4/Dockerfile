FROM python:3.10-slim
WORKDIR /usr/src/app
COPY requirements.txt app4.py .
RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app4.py"]
