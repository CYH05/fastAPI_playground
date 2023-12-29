from abc import ABC, abstractmethod

from src.domain.repositories.item_repository import ItemRepositoryInterface

class ItemUsecaseInterface(ABC):
    
    def __init__(self, repository: ItemRepositoryInterface) -> None:
        self.repository = repository
    
