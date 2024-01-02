from fastapi import FastAPI, Response
from prisma import Prisma
from convert_HTTP_status_code import change_status_code

from src.external.drivers.prisma.prisma_item_service import PrismaItemService
from src.domain.entities.item_entity import Item
from src.domain.usecases.item_usecase import ItemUsecase
from src.external.datasources.item_datasource import ItemDatasource
from src.infra.repositories.item_repository import ItemRepository
from prismaClient.client import PrismaClient


app = FastAPI()

prisma = PrismaClient()

client = Prisma()
service = PrismaItemService(client)
datasource = ItemDatasource(service)
repository = ItemRepository(datasource)
use_case = ItemUsecase(repository)

@app.get('/')
async def read_root():
    return {"Tip": "Access the url 127.0.0.1/8000/docs, to get a better view from the end points"}

@app.get('/items')
async def list_items() -> list[Item]:
    items = await use_case.getAll()
    return items

@app.get('/items/{item_id}')
async def read_item(item_id: int) -> Item:
    item = await use_case.getItem(item_id)
    return item


@app.post('/items/')
async def register_item(item: dict, response: Response) -> dict:
    item = await use_case.createItem(item)
    if 'status' in item:
        change_status_code(item['status'], response)
    return item
    

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