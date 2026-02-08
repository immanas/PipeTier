# 1. Base image (official, stable)
FROM python:3.12-slim
# 2. Set working directory inside container
WORKDIR /app
# 3. Copy dependency file first (cache-friendly)
COPY requirements.txt .
# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# 5. Copy application code
COPY app.py .
# 6. Expose Flask port
EXPOSE 5000
# 7. Start the application
CMD ["python", "app.py"]
