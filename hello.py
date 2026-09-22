from config import ask
from schemas import Recipe
from pydantic import ValidationError
awful_inputs = [
    "",
    "🍳🥚🔥" * 200,
    "word " * 5000,
    "म एउटा recipe चाहन्छु but keep it simple please, दाल भात बनाउने तरिका",
]
a=0
for i in awful_inputs:
    try:
        a=a+1
        print(f"Case{a}")
        reply =ask(i,schema=Recipe)
        recipe=Recipe.model_validate_json(reply)
        print(recipe)
    except ValidationError as e:
        print("Validation error: ",e)
    except Exception as e:
        print(f"Caught{type(e).__name__}: {e}")