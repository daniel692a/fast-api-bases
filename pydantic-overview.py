from pydantic import BaseModel, validator, ValidationError
from typing import Optional

class User(BaseModel):
    # Todos son requeridos
    username:str
    password:str
    repeat_password:str
    email:str
    # Si queremos uque sea opcional, debemos usar el módulo typing
    age: Optional[int] = None

    @validator('username')
    def username_is_valid(cls, username):
        if len(username) < 3:
            raise ValueError('username must be at least 3 characters')
        elif len(username) > 50:
            raise ValueError('username must be at most 50 characters')
        return username

    @validator('repeat_password')
    #values es un diccionario con los atributos del objetos
    def password_is_valid(cls, repeat_password, values):
        if repeat_password != values['password']:
            raise ValueError("passwords don't match")
        return repeat_password


#BaseModel transforma los valores a los que declaramos en la clase

try:
    daniel692a = User(username='daniel692', password='12345', email='123', repeat_password='12345')

    gfa = User(username='gfa', password='1234', email='123', repeat_password='12345')

    print(daniel692a)
except ValidationError as err:
    print(err.json())