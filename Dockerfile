FROM python:3.8

COPY ./requirements.txt /webapp/requirements.txt
COPY /webapp/roberta-sequence-classification-9.onnx /webapp

WORKDIR /webapp

RUN pip install -r requirements.txt

COPY webapp/* /webapp

ENTRYPOINT [ "python" ]

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
