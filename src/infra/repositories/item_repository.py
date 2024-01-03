
from typing import Union

from src.domain.exceptions.exception import AbstractBaseException, DuplicatedRegisterException, InvalidDataFormatException, MissingDataException, EntityNotFoundException
from src.infra.datasources.item_datasource import ItemDatasourceInterface
from src.domain.entities.item_entity import Item
from src.domain.repositories.item_repository import ItemRepositoryInterface

class ItemRepository(ItemRepositoryInterface):
    
    def __init__(self, ds: ItemDatasourceInterface) -> None:
        super().__init__(ds)
        
    async def findByID(self, item_id: int) -> Item:
        try:
            response = await self.datasource.findByID(item_id)
        except EntityNotFoundException as e:    
            response = {'message': e.message, 'status': e.status}            
        
        return response
    
    async def findAll(self) -> list[Item]:
        return await self.datasource.findAll()
    
    async def createItem(self, data: dict) -> dict:
        try:
            response = await self.datasource.createItem(data)
        except InvalidDataFormatException as e:
            response = {'message': e.message, 'status': e.status}
        except MissingDataException as e:
            response = {'message': e.message, 'status': e.status}
        except DuplicatedRegisterException as e:
            response = {'message': e.message, 'status': e.status}
        return response
    
    async def updateItem(self, id: int, data: dict) -> dict:
        try:
            response = await self.datasource.updateItem(id, data)
        except EntityNotFoundException as e:
            response = {'message': e.message, 'status': e.status}  
        except InvalidDataFormatException as e:
            response = {'message': e.message, 'status': e.status}
        except MissingDataException as e:
            response = {'message': e.message, 'status': e.status}
            
        return response