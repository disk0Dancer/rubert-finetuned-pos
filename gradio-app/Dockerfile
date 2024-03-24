FROM python:3.12

EXPOSE 7860/tcp

# COPY ./requirements.txt ./requirements.txt
COPY . /gradio-app/
WORKDIR ./gradio-app

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt \
    && rm -rf /root/.cache/pip

CMD ["python", "app.py"] 