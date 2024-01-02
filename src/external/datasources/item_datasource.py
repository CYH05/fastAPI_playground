from typing import Union

from src.domain.exceptions.exception import AbstractBaseException
from src.domain.entities.item_entity import Item
from src.infra.datasources.item_datasource import ItemDatasourceInterface
from src.external.utils.validators import validadeData


class ItemDatasource(ItemDatasourceInterface):
    
    def __init__(self, dbs) -> None:
        super().__init__(dbs)
        
    async def findByID(self, item_id: int) -> Item:
        return await self.database_service.get(item_id)
    
    async def findAll(self) -> list[Item]:
        return await self.database_service.getAll()
    
    async def createItem(self, data: dict) -> Union[AbstractBaseException, dict]:
        validadeData(data)
        response = await self.database_service.create(data)
        return response
