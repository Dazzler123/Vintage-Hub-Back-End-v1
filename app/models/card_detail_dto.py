from pydantic import BaseModel


class CardDetailDTO(BaseModel):
    id: int
    name: str
    image: None

    # def __init__(self, Id, name, image):
    #     self.id = Id
    #     self.name = name
    #     self.image = image
