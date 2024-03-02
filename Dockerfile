FROM python:3.9.11-slim

ENV PORT {PORT}
ENV ENV {ENV}

WORKDIR /usr/apps/aakriti-sms-spam-classifier

COPY requirements.txt .

RUN apt-get update && apt install build-essential -y --no-install-recommends

RUN python3 -m pip install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000-12000

# CMD ["python3", "config/deps_installer.py", "&&", "python3", "api.py"]

CMD ["make", "start-api"]
