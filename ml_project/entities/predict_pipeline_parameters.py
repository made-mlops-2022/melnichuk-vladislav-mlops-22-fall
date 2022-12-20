from dataclasses import dataclass
from typing import Optional

from .download_parameters import DownloadParameters
from .feature_parameters import FeatureParameters
from marshmallow_dataclass import class_schema
import yaml


@dataclass()
class PredictPipelineParameters:
    path_input_data: str
    path_output_data: str
    model_path: str
    model_type: str
    feature_parameters: FeatureParameters
    downloading_params: Optional[DownloadParameters] = None
    use_mlflow: bool = False
    mlflow_uri: str = "http://79.139.220.13/"
    mlflow_experiment: str = "inference_demo"


PredictPipelineParametersSchema = class_schema(PredictPipelineParameters)


def read_predict_pipeline_parameters(path: str) -> PredictPipelineParameters:
    with open(path, "r") as input_stream:
        schema_predict = PredictPipelineParametersSchema()
        return schema_predict.load(yaml.safe_load(input_stream))
