import asyncio
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from prisma import Prisma

app = FastAPI()

prisma = Prisma()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get('/')
async def read_root():
    return {"Hello": "World"}

@app.get('/items')
async def list_items():
    await prisma.connect()
    items = await prisma.item.find_many()
    await prisma.disconnect()
    return {"items:": items}

@app.get('/items/{item_id}')
async def read_item(item_id: int):
    await prisma.connect()
    item = await prisma.item.find_unique(
        where={
            'id':item_id
        }
    )
    await prisma.disconnect()
    return {"item_id": item}


@app.post('/items/')
async def register_item(item: Item):
    await prisma.connect()
    await prisma.item.create(
        data={
            "name": item.name,
            "price": item.price,
            "isOffer" : item.isOffer
        }
    )
    await prisma.disconnect()
    return {"Message": "Item adicionado com sucesso"}
    

@app.put('/items/{item_id}')
async def update_item(item_id: int, itemModel: Item):
    await prisma.connect()
    await prisma.item.update(
        where={
            'id': item_id
        },
        data={
            'name': itemModel.name,
            'price': itemModel.price,
            'isOffer': itemModel.is_offer
        }
    )
    await prisma.disconnect()
    return{'Message":"Produto '+itemModel.name+' alterado'}

@app.delete('/items/{item_id}')
async def delete_item(item_id: int):
    await prisma.connect()
    await prisma.item.delete(
        where={
            'id': item_id
        }
    )
    await prisma.disconnect()
    return {'Message': 'Produto removido com sucesso'}