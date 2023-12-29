from prisma import Prisma

class PrismaClient():
    connectionState: bool
    client: Prisma = Prisma()
    
    async def changeConnection(self, action: bool) -> None:
        if self.client.is_connected() and not action:
            await self.client.disconnect()
        else:
            await self.client.connect()
        return