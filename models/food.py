from pydantic import BaseModel

class Food(BaseModel):
    id: int
    name: str
    moisture: float 
    kcal: int | None
    kJ: int | None
    protein: float | None
    lipids: float | None
    cholesterol: float | None
    carbohydrate: float | None
    fiber: float | None
    ashes: float | None
    calcium: float | None
    magnesium: float | None
    taco_id: int 
    manganese: float | None
    phosphorus: float | None
    iron: float | None
    sodium: float | None
    potassium: float | None
    copper: float | None
    zinc: float | None
    retinol: float | None
    re: float | None
    rae: float | None
    thiamine: float | None
    riboflavin: float | None
    pyridoxine: float | None
    niacin: float | None
    vitamin_c: float | None
    