Search API Documentation
========================

This endpoint allows you to search for foods based on their name and calorie range.

GET /search
-----------

### Query Parameters

* **name** (required, `string`): The name or part of the name of the food item to search for.  
    Example: `apple` _Case-insensitive search._
* **min_calories** (optional, `integer`, default: `0`): The minimum number of calories to filter the search results.  
    Example: `100`
* **max_calories** (optional, `integer`, default: `10000`): The maximum number of calories to filter the search results.  
    Example: `500`

### Headers

* **X-RateLimit-Limit**: 200 requests per hour.  
    Example: Make no more than 200 API calls to this endpoint within an hour.

### Response

The API returns a JSON array of food items that match the search criteria.

#### Response Model

\[
    {
        "id": 1,
        "name": "Apple",
        "moisture": 85.6,
        "kcal": 52,
        "kJ": 218,
        "protein": 0.3,
        "lipids": 0.2,
        "cholesterol": 0.0,
        "carbohydrate": 13.8,
        "fiber": 2.4,
        "ashes": 0.3,
        "calcium": 6,
        "magnesium": 5,
        "manganese": 0.035,
        "phosphorus": 10,
        "iron": 0.12,
        "sodium": 1,
        "potassium": 107,
        "copper": 0.027,
        "zinc": 0.04,
        "retinol": 0,
        "re": 0,
        "rae": 0,
        "thiamine": 0.017,
        "riboflavin": 0.026,
        "pyridoxine": 0.041,
        "niacin": 0.091,
        "vitamin_c": 4.6
    }
\]
    

#### Status Codes

* 200 OK: The request was successful, and the results are returned.
* 400 Bad Request: Invalid input (e.g., non-numeric calorie range).
* 429 Too Many Requests: The rate limit (200 requests per hour) has been exceeded.

### Notes

* The `name` search uses case-insensitive filtering and supports partial matches.
* Calorie filtering (`min_calories` and `max_calories`) ensures that only foods within the specified calorie range are returned.
* The data is retrieved from the `TACO` dataset and converted to JSON for the response.