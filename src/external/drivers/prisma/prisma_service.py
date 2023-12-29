from abc import ABC, abstractmethod

from prisma import Prisma

class PrismaService(ABC):
    
    def __init__(self, client: Prisma) -> None:
        self.client = client
    
    @abstractmethod
    async def getAll(self):
        raise NotImplemented    

    @abstractmethod
    async def get(self, id: int):
        raise NotImplemented