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
        item = await self.client.item.find_unique(
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
        return {"Response":{"status": 200, "message": "Item Adicionado com sucesso"}}
    
    async def changeConnection(self, action: bool) -> None:
        if self.client.is_connected() and not action:
            await self.client.disconnect()
        else:
            await self.client.connect()
        return
    
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