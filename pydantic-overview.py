from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    # Todos son requeridos
    username:str
    password:str
    email:str
    # Si queremos uque sea opcionla, debemos usar el módulo typing
    age: Optional[int] = None

#BaseModel transforma los valores a los que declaramos en la clase
daniel692a = User(username='daniel692', password='12345', email='123')

print(daniel692a)