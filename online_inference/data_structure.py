from typing import Literal
from pydantic import BaseModel, validator


class DataMedicalOnlineInference(BaseModel):
    age: float
    sex: Literal[0, 1]
    cp: Literal[0, 1, 2, 3]
    trestbps: float
    chol: float
    fbs: Literal[0, 1]
    restecg: Literal[0, 1, 2]
    thalach: float
    exang: Literal[0, 1]
    oldpeak: float
    slope: Literal[0, 1, 2]
    ca: Literal[0, 1, 2, 3]
    thal: Literal[0, 1, 2]

    @validator('age')
    def age_validator(cls, value):
        if value < 1 or value > 90:
            raise ValueError('Wrong Age!')
        return value

    @validator('trestbps')
    def trestbps_validator(cls, value):
        if value < 50 or value > 210:
            raise ValueError('Wrong Trestbps!')
        return value

    @validator('chol')
    def chol_validator(cls, value):
        if value < 60 or value > 600:
            raise ValueError('Wrong Chol!')
        return value

    @validator('thalach')
    def thalach_validator(cls, value):
        if value < 50 or value > 250:
            raise ValueError('Wrong thalach!')
        return value

    @validator('oldpeak')
    def oldpeak_validator(cls, value):
        if value < 0 or value > 8:
            raise ValueError('Wrong Oldpeak!')
        return value
