FROM python:3.10

COPY . /src
RUN pip install -r /src/requirements.txt
RUN cd /src && pyinstaller --onefile --windowed main.py


