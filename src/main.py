from typing import List
from fastapi import FastAPI, HTTPException, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.middleware.cors import CORSMiddleware
from json import loads
from models.food import Food
import pandas as pd

TACO = pd.read_csv("src/data/taco.csv", encoding = 'utf8')

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/search', response_model=List[Food])
@limiter.limit("200/hour")
async def search(request: Request,name: str, min_calories: int = 0, max_calories: int = 10000):
    filter_names = TACO[TACO.name.str.contains(name,na=False, case=False)]
    filter_min_calories = filter_names[filter_names.kcal.astype(int,errors='ignore') >= min_calories]
    filter_max_calories = filter_min_calories[filter_names.kcal.astype(int,errors='ignore') <= max_calories]
    return loads(filter_max_calories.to_json(orient='records'))

