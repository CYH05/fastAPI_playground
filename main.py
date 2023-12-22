from fastapi import FastAPI
from entity.itemModel import Item
from prismaClient.client import PrismaClient

app = FastAPI()

prisma = PrismaClient()


@app.get('/')
async def read_root():
    return {"Hello": "World"}

@app.get('/items')
async def list_items():
    await prisma.changeConnection()
    items = await prisma.client.item.find_many()
    await prisma.changeConnection()
    return {"items:": items}

@app.get('/items/{item_id}')
async def read_item(item_id: int):
    await prisma.changeConnection()
    item = await prisma.client.item.find_unique(
        where={
            'id':item_id
        }
    )
    await prisma. changeConnection()
    return {"item_id": item}


@app.post('/items/')
async def register_item(item: Item):
    await prisma.changeConnection()
    await prisma.client.item.create(
        data={
            "name": item.name,
            "price": item.price,
            "isOffer" : item.isOffer
        }
    )
    await prisma.changeConnection()
    return {"Message": "Item adicionado com sucesso"}
    

@app.put('/items/{item_id}')
async def update_item(item_id: int, itemModel: Item):
    await prisma.changeConnection()
    await prisma.item.update(
        where={
            'id': item_id
        },
        data={
            'name': itemModel.name,
            'price': itemModel.price,
            'isOffer': itemModel.isOffer
        }
    )
    await prisma.changeConnection()
    return{'Message":"Produto '+itemModel.name+' alterado'}

@app.delete('/items/{item_id}')
async def delete_item(item_id: int):
    await prisma.changeConnection()
    await prisma.client.item.delete(
        where={
            'id': item_id
        }
    )
    await prisma.changeConnection()
    return {'Message': 'Produto removido com sucesso'}