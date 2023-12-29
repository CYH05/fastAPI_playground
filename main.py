from fastapi import FastAPI
from src.external.drivers.prisma.prisma_item_service import PrismaItemService
from src.domain.entities.item_entity import Item
from src.domain.usecases.item_usecase import ItemUsecase
from src.external.datasources.item_datasource import ItemDatasource
from src.infra.repositories.item_repository import ItemRepository
from prismaClient.client import PrismaClient
from prisma import Prisma

app = FastAPI()

prisma = PrismaClient()


@app.get('/')
async def read_root():
    return {"Hello": "World"}

@app.get('/items')
async def list_items():
    await prisma.changeConnection(True)
    items = await prisma.client.item.find_many()
    await prisma.changeConnection(False)
    return {"items:": items}

@app.get('/items/{item_id}')
async def read_item(item_id: int):
    client = Prisma()
    service = PrismaItemService(client)
    datasource = ItemDatasource(service)
    repository = ItemRepository(datasource)
    use_case = ItemUsecase(repository)
    
    item = await use_case.getItem(item_id)
    return item


@app.post('/items/')
async def register_item(item: Item):
    await prisma.changeConnection(True)
    await prisma.client.item.create(
        data={
            "name": item.name,
            "price": item.price,
            "is_offer" : item.is_offer
        }
    )
    await prisma.changeConnection(False)
    return {"Message": "Item adicionado com sucesso"}
    

@app.put('/items/{item_id}')
async def update_item(item_id: int, itemModel: Item):
    await prisma.changeConnection(True)
    await prisma.item.update(
        where={
            'id': item_id
        },
        data={
            'name': itemModel.name,
            'price': itemModel.price,
            'is_offer': itemModel.is_offer
        }
    )
    await prisma.changeConnection(False)
    return{'Message":"Produto '+itemModel.name+' alterado'}

@app.delete('/items/{item_id}')
async def delete_item(item_id: int):
    await prisma.changeConnection(True)
    await prisma.client.item.delete(
        where={
            'id': item_id
        }
    )
    await prisma.changeConnection(False)
    return {'Message': 'Produto removido com sucesso'}