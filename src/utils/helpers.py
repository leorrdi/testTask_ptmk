from datetime import date, timedelta
from data.full_names import names
from typing import TYPE_CHECKING
import random


if TYPE_CHECKING:
    from src.employee import Gender
    

def convert_to_date(date_string: str) -> date:
    try:
        return date.fromisoformat(date_string)
    except ValueError as e:
        print(f"Не удалось преобразовать строку в дату. Попробуйте еще раз в формате: ГГГГ-ММ-ДД")
        return None
    

def get_random_gender() -> 'Gender':
    from src.employee import Gender
    
    return random.choice(list(Gender))


def generate_full_name(gender: 'Gender') -> str:
    if  gender.value == "male":
        first_name = random.choice(names["male_first_names"])
        last_name = random.choice(names["male_last_names"])
        middle_name = random.choice(names["male_middle_names"])
    elif gender.value == "female":
        first_name = random.choice(names["female_first_names"])
        last_name = random.choice(names["female_last_names"])
        middle_name = random.choice(names["female_middle_names"])
    
    return "{0} {1} {2}".format(first_name, last_name, middle_name)


def generate_birthday(start_date:date, end_date:date) -> date:
    difference = end_date - start_date
    return start_date + timedelta(random.randint(0, difference.days))


def generate_full_name_with_F() -> str:
    first_name = random.choice(names["male_first_names"])
    last_name = random.choice(names["male_last_names_in_F"])
    middle_name = random.choice(names["male_middle_names"])

    return "{0} {1} {2}".format(first_name, last_name, middle_name)


