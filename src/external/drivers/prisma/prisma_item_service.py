from prisma import Prisma

from src.domain.entities.item_entity import Item
from src.external.drivers.prisma.prisma_service import PrismaService


class PrismaItemService(PrismaService):
    
    def __init__(self, client: Prisma) -> None:
        super().__init__(client)
        
    async def getAll(self) -> list[Item]:
        await self.changeConnection(True)
        items = await self.client.item.find_many()
        await self.changeConnection(False)
        return items
        
    async def get(self, id: int) -> Item:
        await self.changeConnection(True)
        item = await self.client.item.find_first(
            where={
                'id':id
            }
        )
        await self.changeConnection(False)
        return {"item_id": item}
    
    async def create(self, data: dict) -> dict:
        await self.changeConnection(True)
        await self.client.item.create(
            data={
                "name": data['name'],
                "price": data['price'],
                "is_offer" : data['is_offer']
            }
        )
        await self.changeConnection(False)
        return {"Response":{"status": 200, "message": "Item adicionado com sucesso."}}
    
    
    async def update(self, id: int, data: dict):
        await self.changeConnection(True)
        await self.client.item.update(
            where={
                'id': id
                },
            data={
                'name': data['name'],
                'price': data['price'],
                'is_offer': data['is_offer'],
            }
        )
        await self.changeConnection(False)
        return {"Response":{"status": 200, "message": "Item alterado com sucesso."}}
    
    async def delete(self, id: int) -> dict:

        # TODO If it's necessary to keep the data for some register, it's possible just turning the field is_offer to false and add the filter is_offer equals true when the list function is called, in these scenario I'll just exclude the register
        await self.changeConnection(True)
        await self.client.item.delete(
            where={
                'id': id
            }
        )
        await self.changeConnection(False)
        return {"Response":{"status": 200, "message": "Item removido com sucesso."}}
    
    async def changeConnection(self, action: bool) -> None:
        if self.client.is_connected() and not action:
            await self.client.disconnect()
        else:
            await self.client.connect()
        return
    
    # TODO validate the ideia to turn thesefunctions checkDupplicity and checkExistence into one, just changing the parameter, recieving a dict to be the body from the attribute where from function find_first
    
    async def checkDupplicity(self, item_data: dict) -> bool:
        await self.changeConnection(True)
        item = await self.client.item.find_first(
            where={
                'name': item_data['name'],
                'price': item_data['price'],
            }
        )
        await self.changeConnection(False)
        
        if item:
            return True
        return False
    
    async def checkExistence(self,  id: int) -> bool:
        await self.changeConnection(True)
        
        item = await self.client.item.find_first(
            where={
                'id':id
            }
            
        )
        await self.changeConnection(False)
        if item:
            return True
        
        return False