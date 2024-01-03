from abc import ABC, abstractmethod

from src.infra.datasources.item_datasource import ItemDatasourceInterface
from src.domain.entities.item_entity import Item

class ItemRepositoryInterface(ABC):
    
    def __init__(self, ds: ItemDatasourceInterface) -> None:
        self.datasource = ds
    
    @abstractmethod
    async def findByID(self, item_id: int) -> Item:
        pass

    @abstractmethod
    def findAll(self) -> list[Item]:
        pass
    
    @abstractmethod
    async def createItem(self, data: dict) -> dict:
        pass
    
    @abstractmethod
    async def updateItem(self, id: int, data: dict) -> dict:
        pass