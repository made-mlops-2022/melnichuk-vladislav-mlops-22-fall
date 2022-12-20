import logging
import pickle
import pandas as pd
import hydra

from data import read_data_pd
from models import (
    predict_model,
)

logger = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="../configs", config_name="predict_config_1_logreg")
def predict_pipeline(config):
    if config.use_mlflow:
        pass
    else:
        return run_prediction_pipeline(config)


def run_prediction_pipeline(config):
    logger.info(f"Start prediction pipeline with parameters {config}")
    test_df = read_data_pd(config.path_input_data)
    logger.info(f"data.shape is {test_df.shape}")
    logger.info(f"model_type is {config.model_type}")

    with open(config.model_path + "model_" + config.model_type + ".pkl", "rb") as file_obj:
        model = pickle.load(file_obj)
        predicts = predict_model(
            model,
            test_df,
            config.feature_parameters.use_logarithm_trick
        )
        predicts_df = pd.DataFrame({config.feature_parameters.target_column: predicts})
        predicts_df.to_csv(config.path_output_data + "prediction_" + config.model_type + ".csv")
        file_obj.close()

    return


if __name__ == "__main__":
    predict_pipeline()
