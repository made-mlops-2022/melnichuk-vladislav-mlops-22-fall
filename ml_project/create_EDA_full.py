import pandas as pd
import os
import logging
import hydra
from pandas_profiling import ProfileReport

logger = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="../configs", config_name="train_config_1_logreg")
def make_eda_full_report(config):
    logger.info(config.path_input_data)
    df = pd.read_csv(config.path_input_data)
    profile = ProfileReport(df, title="EDA_full")
    profile.to_file(
        os.path.join("reports/EDA/", "EDA_full_report.html")
    )


if __name__ == "__main__":
    make_eda_full_report()
