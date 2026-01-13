FROM python:3.13.3-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY .env .
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
COPY my_twitter .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
