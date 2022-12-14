# run.sh ver 1.3
if [ -z $MODEL_PATH ]
then
    export MODEL_PATH="LogReg_model_1.pkl"
    export FILE_ID="1EftDfAMyZALFYWexVEZyLBN7IF6abzAL"
    export FILE_NAME=MODEL_PATH
fi

if [[ ! -f $MODEL_PATH ]]
then
    # not working variant for big files from google disk
    # FILE_ID="1EftDfAMyZALFYWexVEZyLBN7IF6abzAL" FILE_NAME=MODEL_PATH wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=$FILE_ID' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=$FILE_ID" -O $FILE_NAME && rm -rf /tmp/cookies.txt
    # wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1EftDfAMyZALFYWexVEZyLBN7IF6abzAL' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=$OUR_ID" -O $MODEL_PATH && rm -rf /tmp/cookies.txt
    
    # another working variant
    # wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1EftDfAMyZALFYWexVEZyLBN7IF6abzAL' -O $MODEL_PATH
    wget 'https://drive.google.com/uc?export=download&id=1EftDfAMyZALFYWexVEZyLBN7IF6abzAL' --output-document=$MODEL_PATH
    echo $MODEL_PATH
else
    echo "Model Exists!"
fi

# uvicorn main_online_inference:app --reload --host 0.0.0.0 --port 12000
uvicorn main_online_inference:app --reload --host 127.0.0.1 --port 12000