
from src.infra.datasources.item_datasource import ItemDatasourceInterface
from src.domain.entities.item_entity import Item
from src.domain.repositories.item_repository import ItemRepositoryInterface

class ItemRepository(ItemRepositoryInterface):
    
    def __init__(self, ds: ItemDatasourceInterface) -> None:
        super().__init__(ds)
        
    async def findByID(self, item_id: int) -> Item:
        return await self.datasource.findByID(item_id)
    
    def create(self, name: str, price: float, is_offer: bool) -> Item:
        item = Item(name=name, price=price, is_offer=is_offer)
        return item
    
    def update(self, item: Item) -> Item:
        return super().update(item)