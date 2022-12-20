# run.sh ver 1.3
if [ -z $MODEL_PATH ]
then
    export MODEL_PATH="LogReg_model_1.pkl"
fi

if [[ ! -f $MODEL_PATH ]]
then
    wget https://drive.google.com/uc?export=download&id=1EftDfAMyZALFYWexVEZyLBN7IF6abzAL --output-document=$MODEL_PATH
    echo $MODEL_PATH
else
    echo "Model Exists!"
fi

uvicorn main_online_inference:app --reload --host 0.0.0.0 --port 12000
