from fastapi import FastAPI, HTTPException
from typing import Annotated
import pandas as pd
from json import loads

app = FastAPI()

taco = pd.read_csv("data/taco.csv", encoding = 'utf8')
amino = pd.read_csv("data/amino.csv", encoding = 'utf8')

@app.get("/search")
async def create(name: str):
    return loads(taco[taco['name'].str.contains(name,na=False, case=False)].to_json(orient='records'))

