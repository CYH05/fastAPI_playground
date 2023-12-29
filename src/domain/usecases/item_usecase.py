from src.domain.repositories.item_repository import ItemRepositoryInterface
from src.domain.usecases.item_usecase_interface import ItemUsecaseInterface

class ItemUsecase(ItemUsecaseInterface):
    
    def __init__(self, repository: ItemRepositoryInterface) -> None:
        super().__init__(repository)
    
    async def getItem(self, item_id: int):
        return await self.repository.findByID(item_id)
        
    async def getAll(self):
        return await self.repository.findAll()
        
