from prisma import Prisma
from src.external.drivers.prisma.prisma_service import PrismaService


class PrismaItemService(PrismaService):
    
    def __init__(self, client: Prisma) -> None:
        super().__init__(client)
        
    async def get(self, id: int):
        await self.changeConnection(True)
        item = await self.client.item.find_unique(
            where={
                'id':id
            }
        )
        await self.changeConnection(False)
        return {"item_id": item}
    
    async def changeConnection(self, action: bool) -> None:
        if self.client.is_connected() and not action:
            await self.client.disconnect()
        else:
            await self.client.connect()
        return