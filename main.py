from fastapi import FastAPI, HTTPException
from typing import Annotated
import pandas as pd
from json import loads

app = FastAPI()

taco = pd.read_csv("data/taco.csv", encoding = 'utf8')
amino = pd.read_csv("data/amino.csv", encoding = 'utf8')

@app.get('')

@app.get('/search')
async def create(name: str, min_calories: int = 0, max_calories: int = 10000):
    filter_names = taco[taco.name.str.contains(name,na=False, case=False)]
    filter_min_calories = filter_names[filter_names.kcal.astype(int) >= min_calories]
    filter_max_calories = filter_min_calories[filter_names.kcal.astype(int) <= max_calories]
    end = filter_max_calories
    return loads(end.to_json(orient='records'))

