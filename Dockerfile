FROM python:3.9.17-alpine3.18
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY Sender.py .
COPY Receiver.py .
CMD python Receiver.py & python Sender.py 
