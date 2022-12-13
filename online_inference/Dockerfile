# Dockerfile ver 1.3
FROM python:3.10-slim-bullseye
RUN python3 -m pip install --upgrade pip

COPY requirements.txt requests data main_online_inference.py data_structure.py run.sh ./online_inference/
WORKDIR /online_inference

RUN apt-get update && apt-get install wget -y
RUN pip3 install -r requirements.txt --no-cache-dir

ENV MODEL_PATH="LogReg_model_1.pkl"

EXPOSE 12000

CMD ["bash", "run.sh"]
