from fastapi import FastAPI, HTTPException, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import pandas as pd
from json import loads

TACO = pd.read_csv("data/taco.csv", encoding = 'utf8')
AMINO = pd.read_csv("data/amino.csv", encoding = 'utf8')

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.get('/search')
@limiter.limit("1000/hour")
async def create(request: Request,name: str, min_calories: int = 0, max_calories: int = 10000):
    filter_names = TACO[TACO.name.str.contains(name,na=False, case=False)]
    filter_min_calories = filter_names[filter_names.kcal.astype(int) >= min_calories]
    filter_max_calories = filter_min_calories[filter_names.kcal.astype(int) <= max_calories]
    end = filter_max_calories
    return loads(end.to_json(orient='records'))

