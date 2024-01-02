from src.domain.exceptions.exception import InvalidDataFormatException, MissingDataException
from src.domain.utils.enum import ItemFields

def validadeData(data: dict) -> None:
    # TODO check if the option 1 is better than option 2
    # option 1: Checking if there are all the required fields from item model (from an enum) inside the data
    # option 2: Looking all the fields from the upcoming data and check if it's in the model (there are only the necessary fields, and denny data with more fields)
    fields = ItemFields
    
    for field in fields:
        if field.name in data:
            if not (type(data[field.name]) == field.value):                     
                raise InvalidDataFormatException(
                        message='O campo {} deve ser do tipo {}, mas recebemos o tipo {}'.format(
                            field.name,
                            field.value, 
                            type(data[field.name])),
                        status=400
                        )
        else:
            raise MissingDataException(
                    message='O campo '+field.name+' não foi informado.',
                    status=400
                    )
