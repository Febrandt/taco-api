from pydantic import BaseModel

class Food(BaseModel):
    id: int
    name: str
    moisture: float | str
    kcal: int | str | None
    kJ: int | str | None
    protein: float | str | None
    lipids: float | str | None
    cholesterol: float | str | None
    carbohydrate: float | str | None
    fiber: float | str | None
    ashes: float | str | None
    calcium: float | str | None
    magnesium: float | str | None
    taco_id: int 
    manganese: float | str | None
    phosphorus: float | str | None
    iron: float | str | None
    sodium: float | str | None
    potassium: float | str | None
    copper: float | str | None
    zinc: float | str | None
    retinol: float | str | None
    re: float | str | None
    rae: float | str | None
    thiamine: float | str| None
    riboflavin: float | str| None
    pyridoxine: float | str| None
    niacin: float | str| None
    vitamin_c: float | str | None
    