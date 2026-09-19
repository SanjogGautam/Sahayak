from pydantic import BaseModel, Field
from typing import Optional, List

class Ingredient(BaseModel):
    name: str = Field(..., description="Name of the ingredient")
    quantity: Optional[str] = Field(None, description="Quantity of the ingredient")
class Recipe(BaseModel):
    title: str = Field(..., description="Title of the recipe")
    description: Optional[str] = Field(None, description="Description of the recipe")
    ingredients: List[Ingredient] = Field(..., description="List of ingredients for the recipe")
    instructions: list[str] 
