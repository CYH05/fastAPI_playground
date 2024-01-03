from abc import ABC, abstractmethod

from prisma import Prisma

from src.domain.entities.item_entity import Item

class PrismaService(ABC):
    
    def __init__(self, client: Prisma) -> None:
        self.client = client
    
    @abstractmethod
    async def getAll(self) -> list[Item]:
        pass    

    @abstractmethod
    async def get(self, id: int) -> Item:
        pass
    
    @abstractmethod
    async def create(self, data: dict) -> dict:
        pass
    
    @abstractmethod
    async def update(self, id: int, data: dict) -> dict:
        pass
    
    @abstractmethod
    async def delete(self, id: int) -> dict:
        pass
    
    @abstractmethod
    async def changeConnection(self, action: bool) -> None:
        pass
    
    @abstractmethod
    async def checkDupplicity(self, item_data: dict) -> bool:
        pass
    
    @abstractmethod
    async def checkExistence(self, id: int) -> bool:
        pass