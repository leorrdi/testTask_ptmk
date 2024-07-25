from datetime import date
from typing import List
from enum import Enum
from src import utils
import timeit


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"


class Employee:
    def __init__(self, full_name:str, birthday:date, gender:Gender) -> None:
        self.full_name = full_name
        self.birthday = birthday
        self.gender = gender


    def calculate_age(self) -> int:
        current_year = date.today().year
        age = current_year - self.birthday.year
        return age
    


def generate_random_employees(amount: int) -> List[Employee]:
    list_employees = []
        
    for _ in range(amount):
        gender = utils.get_random_gender()
        full_name = utils.generate_full_name(gender)
        birthday = utils.generate_birthday(date(1960,1,1), date(2006,1,1))

        list_employees.append(Employee(full_name, birthday, gender))
        
    return list_employees


def generate_employees_witch_F(amount: int) -> List[Employee]:
    list_employees = []

    for _ in range(amount):
        gender = Gender.MALE
        full_name = utils.generate_full_name_with_F()
        birthday = utils.generate_birthday(date(1960,1,1), date(2006,1,1))

        list_employees.append(Employee(full_name, birthday, gender))

    return list_employees