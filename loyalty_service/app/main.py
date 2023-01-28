from fastapi import FastAPI, HTTPException

class Loyalty:
    def __init__(self, id: int, status: str, nameLoyalty: str):
        self.id = id
        self.status = status
        self.name = nameLoyalty

loyaltyList: list[Loyalty] = [
    Loyalty(0, 'Активно', 'Скидка %30 на бытовую технику'),
    Loyalty(1, 'Использовано', 'Скидка %15 на электронику'),
    Loyalty(2, 'Срок действия истек', 'Скидка %10 на продуктовые товары')
]

app = FastAPI()


@app.get("/v1/loyalties")
async def get_loyalties():
    return loyaltyList

@app.get("/v1/loyalties/{id}")
async def get_loyalties_by_id(id: int):
    result = [item for item in loyaltyList if item.id == id]
    if len(result) > 0:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail="Loyalties not found")