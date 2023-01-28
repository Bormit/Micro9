from fastapi import FastAPI, HTTPException

class Status:
    def __init__(self, id: int, status: str, listOrder: str):
        self.id = id
        self.status = status
        self.listOrder = listOrder

statusList: list[Status] = [
    Status(0, 'Создан', 'Microwave'),
    Status(1, 'Оплачен', 'Cat food'),
    Status(2, 'Ожидает оплаты', 'Fridge')
]

app = FastAPI()


@app.get("/v1/orders")
async def get_orders():
    return statusList

@app.get("/v1/orders/{id}")
async def get_orders_by_id(id: int):
    result = [item for item in statusList if item.id == id]
    if len(result) > 0:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail="Orders not found")

