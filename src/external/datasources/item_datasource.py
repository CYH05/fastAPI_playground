from src.domain.exceptions.exception import DuplicatedRegisterException
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
    
    async def createItem(self, data: dict) -> dict:
        validadeData(data)
        if await self.database_service.checkDupplicity(data):
            raise DuplicatedRegisterException(
                message='Há um item com o mesmo nome e preço cadastrado.',
                status=400
            )
        response = await self.database_service.create(data)
        return response
