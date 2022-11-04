from fastapi import FastAPI
import torch
import numpy as np
from transformers import RobertaTokenizer
import onnxruntime

app = FastAPI()
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
session = onnxruntime.InferenceSession("../webapp/model/roberta-sequence-classification-9.onnx")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict")
def predict(text: str):
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
    input_ids = torch.tensor(tokenizer.encode(text, add_special_tokens=True)).unsqueeze(0)  # Batch size 1

    ort_inputs = {session.get_inputs()[0].name: to_numpy(input_ids)}
    ort_out = session.run(None, ort_inputs)
    print(ort_out) #Result console

    pred = np.argmax(ort_out)
    if(pred == 0):
        return {"Prediction": "Negative"}
    elif(pred == 1):
        return {"Prediction": "Positive"}


def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


