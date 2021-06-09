FROM python:latest

# Dependencies
RUN apt update > /dev/null 2>&1
RUN apt install chromium -y > /dev/null 2>&1
RUN apt install wget unzip curl -y > /dev/null 2>&1

RUN version=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$(chromium --version | grep -oP 'Chromium \K\d+')) && \
    wget https://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip -d /usr/bin > /dev/null 2>&1
RUN rm chromedriver_linux64.zip

# Setup for app.py
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]