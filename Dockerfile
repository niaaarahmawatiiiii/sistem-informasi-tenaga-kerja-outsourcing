# Gunakan base image python yang ringan
FROM python:3.11-slim

# Set working directory di dalam container
WORKDIR /app

# Salin file dependencies dan install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode project ke dalam container
COPY . .

# Jalankan server FastAPI 
# 'backend.main:app' artinya masuk ke folder backend, buka main.py, dan ambil variabel app
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
