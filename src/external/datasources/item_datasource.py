from src.domain.exceptions.exception import DuplicatedRegisterException, EntityNotFoundException
from src.domain.entities.item_entity import Item
from src.infra.datasources.item_datasource import ItemDatasourceInterface
from src.external.utils.validators import validadeData


class ItemDatasource(ItemDatasourceInterface):
    
    def __init__(self, dbs) -> None:
        super().__init__(dbs)
        
    async def findByID(self, item_id: int) -> Item:
        if not await self.database_service.checkExistence(item_id):
            raise EntityNotFoundException(
                message='O registro com ID {} não existe.'.format(item_id),
                status=400
            )
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

    async def updateItem(self, id: int, data: dict) -> dict:
        validadeData(data)
        item = await self.database_service.checkExistence(id)
        if not item:
            raise EntityNotFoundException(
                message='O registro com ID {} não existe.'.format(id),
                status=400
            )
        return await self.database_service.update(id, data)