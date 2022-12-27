import json
import logging
import hydra

from data import read_data_pd, split_data_train_val
from features.build_features_train import gain_target
from models import (
    train_model,
    model_serialize,
    predict_model,
    evaluate_model
)

logger = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="../configs", config_name="train_config_1_logreg")
def train_pipeline_start(config):
    if config.use_mlflow:
        pass
    else:
        return run_training_pipeline(config)


def run_training_pipeline(config):
    logger.info(f"Start training pipeline with parameters {config}")
    data = read_data_pd(config.path_input_data)
    logger.info(f"data.shape is {data.shape}")
    train_df, val_df = split_data_train_val(
        data, config.split_parameters
    )

    val_target = gain_target(val_df, config.feature_parameters)
    train_target = gain_target(train_df, config.feature_parameters)
    train_df = train_df.drop(config.feature_parameters.target_column, axis=1)
    val_df = val_df.drop(config.feature_parameters.target_column, axis=1)

    val_target.to_csv(config.path_test_target, index=False)
    train_target.to_csv(config.path_train_target, index=False)
    train_df.to_csv(config.path_train_features, index=False)
    val_df.to_csv(config.path_test_features, index=False)
    logger.info(f"train_df.shape is {train_df.shape}")
    logger.info(f"val_df.shape is {val_df.shape}")

    # test
    # print("train_df is \n", train_df)
    # print("train_target is \n", train_target)

    model = train_model(
        train_df, train_target, config.train_parameters
    )
    predicts = predict_model(
        model,
        val_df,
        config.feature_parameters.use_logarithm_trick,
    )
    metrics = evaluate_model(
        predicts,
        val_target,
        config.feature_parameters.use_logarithm_trick,
    )
    with open(config.metric_path + "metrics_" + config.train_parameters.model_type + ".json", "w") as metric_file:
        json.dump(metrics, metric_file)
    logger.info(f"metrics is {metrics}")

    path_to_model = model_serialize(
        model, config.output_model_path + "model_" + config.train_parameters.model_type + ".pkl"
    )
    return path_to_model, metrics


if __name__ == "__main__":
    train_pipeline_start()
