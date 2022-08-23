from pydantic import BaseModel


class Author(BaseModel): # pydantic.BaseModel
    name: str
    age: int

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "age": 42,
            }
        } # example data for schema generation


class Book(BaseModel): # pydantic.BaseModel
    """
    pydantic automatically generates schema 
    for this class based on the fields 
    defined in the class definition above (Author) 
    and the Config class above (schema_extra)
    """
    name: str # name of the book
    author: Author # pydantic.BaseModel
    genre: str 
    released: bool = False # default value for released field
    price: float # decimal number

    class Config:
        schema_extra = {
            "example": {
                "name": "The Art of Computer Programming",
                "author": {
                    "name": "Donald Knuth",
                    "age": 70
                },
                "genre": "Computer Science",
                "released": True,
                "price": 39.99
            } 
        } # example data for schema generation
    
    def __str__(self):
        return f"{self.name} by {self.author.name}"
    
    def __repr__(self):
        return f"{self.name} by {self.author.name}"
