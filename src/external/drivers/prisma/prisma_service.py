from abc import ABC, abstractmethod
from typing import Union

from prisma import Prisma

from src.domain.exceptions.exception import AbstractBaseException
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
    async def create(self, data: dict) -> Union[AbstractBaseException, dict]:
        pass