from prisma import Prisma

class PrismaClient():
    connectionState: bool
    client: Prisma = Prisma()
    
    async def changeConnection(self) -> None:
        if self.client.is_connected():
            await self.client.disconnect()
        else:
            await self.client.connect()
        return