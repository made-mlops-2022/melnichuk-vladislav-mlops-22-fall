from typing import Optional
from dataclasses import dataclass

from .download_parameters import DownloadParameters
from .split_parameters import SplitParameters
from .feature_parameters import FeatureParameters
from .train_parameters import TrainParameters
from .model_parameters import RandomForestParameters, LogRegParameters
from .transform_parameters import TransformParameters
from marshmallow_dataclass import class_schema
from hydra.core.config_store import ConfigStore
import yaml


@dataclass()
class TrainPipelineParameters:
    path_input_data: str
    output_model_path: str
    metric_path: str
    path_train_features: str
    path_train_target: str
    path_test_features: str
    path_test_target: str
    split_parameters: SplitParameters
    feature_parameters: FeatureParameters
    train_parameters: TrainParameters
    transform_params: Optional[TransformParameters] = None
    downloading_params: Optional[DownloadParameters] = None
    use_mlflow: bool = False
    mlflow_uri: str = "http://79.139.220.13/"
    mlflow_experiment: str = "inference_demo"


TrainPipelineParametersSchema = class_schema(TrainPipelineParameters)


def read_train_pipeline_parameters(path: str) -> TrainPipelineParameters:
    with open(path, "r") as input_stream:
        schema_train = TrainPipelineParametersSchema()
        return schema_train.load(yaml.safe_load(input_stream))


def register_configs_train() -> None:
    config_store = ConfigStore.instance()
    config_store.store(name="config", node=TrainPipelineParameters)
    config_store.store(
        group="model",
        name="rf",
        node=RandomForestParameters
    )
    config_store.store(
        group="model",
        name="logreg",
        node=LogRegParameters
    )
