import os
import sys

sys.path.append(os.path.join(os.path.abspath("."), "ml_project/"))
sys.path.append("../")


def test_train_inference():
    exit_error_status_train = os.system(
        "python ml_project/train_pipeline_full.py")
    exit_error_status_predict = os.system(
        "python ml_project/predict_pipeline_full.py")
    assert exit_error_status_train == 0
    assert exit_error_status_predict == 0
