FROM python:3.8

COPY requirements.txt /tmp/

RUN pip install --requirement /tmp/requirements.txt


EXPOSE 8000

COPY ./webapp /webapp

CMD ["uvicorn", "webapp.app:app", "--host", "0.0.0.0", "--port", "8000"]
