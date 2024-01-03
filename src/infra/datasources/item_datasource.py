from abc import ABC, abstractmethod

from src.domain.entities.item_entity import Item
from src.external.drivers.prisma.prisma_service import PrismaService

class ItemDatasourceInterface(ABC):
    
    def __init__(self, dbs: PrismaService) -> None:
        """As I'm using prisma, here I define the type of dbs as a abstract class of prisma, but it's not necessary a prisma instance """
        self.database_service = dbs
    
    @abstractmethod
    async def findByID(self, item_id: int) -> Item:
        pass
    
    @abstractmethod
    async def findAll(self) -> list[Item]:
        pass
    
    @abstractmethod
    async def createItem(self, data: dict) -> dict:
        pass
    
    @abstractmethod
    async def updateItem(self, id: int, data: dict) -> dict:
        pass