import os
import pickle

import pandas as pd
from fastapi import FastAPI
from fastapi_health import health

from data_structure import DataMedicalOnlineInference

app = FastAPI()

# make non global
model = None


@app.on_event('startup')
def load_model():
    model_path = os.getenv('MODEL_PATH')

    with open(model_path, 'rb') as f:
        global model
        model = pickle.load(f)

@app.post('/predict')
async def predict(data: DataMedicalOnlineInference):
    data_df = pd.DataFrame([data.dict()])
    y = model.predict(data_df)
    print(y)
    return {'condition': 'disease' if y[0] == 1 else 'no disease'}


@app.get('/')
def home():
    return {"key": "Neural Networks work!"}


async def handler_successed(**kwargs):
    return 'Model is ready!'


async def handler_failed(**kwargs):
    return 'Model is being prepared, wait!'


def is_ready():
    return model is not None

app.add_api_route('/health', health([is_ready],
                  success_handler=handler_successed,
                  failure_handler=handler_failed))
