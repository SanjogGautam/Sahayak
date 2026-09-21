from pydantic import ValidationError
from schemas import Recipe

bad_replies = [
    '{"title": "Cookies", "instructions": ["mix", "bake"]}',           # missing ingredients
    '{"title": "Cookies", "ingredients": "flour, sugar", "instructions": ["mix"]}',  # wrong type
    '{"title": "Cookies", "ingredients": [], "instructions": "mix"}',  # instructions not a list
]

for reply in bad_replies:
    try:
        Recipe.model_validate_json(reply)
        print("passed validation (unexpected)")
    except ValidationError as e:
        print(e)