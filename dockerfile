FROM python:3.9-slim-buster

#WORKDIR /SimulationOriginAI


RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "uvicorn", "--host", "0.0.0.0" , "main:app", "--reload"]




