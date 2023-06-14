from typing import Union

from fastapi import FastAPI

import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ilert")
def read_ilert():
    url = 'https://api.ilert.com/api/numbers'
    headers = {'Accept': 'application/json'}
    r = requests.get(url, headers=headers)
    return {"status": r.status_code, "body": r.json()}


@app.get("/api/health")
def read_root():
    return {"ok": True}
