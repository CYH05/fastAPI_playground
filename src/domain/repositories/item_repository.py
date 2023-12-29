from abc import ABC, abstractmethod
from src.infra.datasources.item_datasource import ItemDatasourceInterface
from src.domain.entities.item_entity import Item

class ItemRepositoryInterface(ABC):
    
    def __init__(self, ds: ItemDatasourceInterface) -> None:
        self.datasource = ds
    
    @abstractmethod
    async def findByID(self, item_id: int) -> Item:
        raise NotImplemented

    @abstractmethod
    def findAll(self) -> list[Item]:
        raise NotImplemented