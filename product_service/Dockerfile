FROM python:3.12-slim

WORKDIR /app

# зависимости отдельным слоем — кешируются, пока не изменится requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
ENV PYTHONPATH=/app/src

EXPOSE 8000
CMD ["uvicorn", "product_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
