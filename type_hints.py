# Annotation types
from typing import List, Tuple, Dict, Union

# vars
name :str = 'Daniel'
age:int = 18
grade:float = 3.5
male:bool = True
print(name)
# functions
def say_my_name(name:str)-> str:
    return f'Hello {name}'

def add(num_1:int, num_2:int)->int:
    return num_1 + num_2

val_1 : int

# classes

class User():
    def __init__(self, name:str, age:int)->None:
        self.name : str = name
        self.age : int = age

    def greeting(self)->str:
        return f'Hello {self.name}'

daniel = User('Daniel', 18)
print(daniel.greeting())


# lists
grades : List[float] = [3.5, 4.0, 3.5, 4.0, 3.5]
names : List[str] = ['Daniel', 'Sandy', 'Marta', 'Mary', 'Sam']

def average(grades: List[float])->float:
    return sum(grades) / len(grades)

print(average(grades))

# Tuples

ages : Tuple[int] = (18, 19, 20, 21, 22)
def show_age(ages:Tuple[int])->None:
    for age in ages:
        print(age)

show_age(ages)

# Para cada valor de la tupla usamos Union
schools : Tuple[Union[str, str, str]] = ('MIT', 'Harvard', 'Yale')

print(schools)


# Dictionaries
# Dict[key_type, value_type]
users : Dict[str, int] = {
    'daniel692a': 10,
    'rodo_ferro': 0
}

