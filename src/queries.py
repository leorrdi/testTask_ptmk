import sqlite3
from typing import List
from .employee import Employee
from .utils import convert_to_date


class DatabaseEmployee:
    connection = sqlite3.connect('data/employee.db')
    cursor = connection.cursor()


    @staticmethod
    def create_table() -> None:
        DatabaseEmployee.drop_table()

        query = """
            CREATE TABLE `employee` (
            id INTEGER PRIMARY KEY,
            full_name TEXT NOT NULL,
            birthday TEXT NOT NULL,
            gender TEXT NOT NULL
            )
        """

        DatabaseEmployee.cursor.execute(query)
        DatabaseEmployee.connection.commit()


    @staticmethod
    def drop_table() -> None:
        query = """ DROP TABLE IF EXISTS `employee` """
        
        DatabaseEmployee.cursor.execute(query)
        DatabaseEmployee.connection.commit()


    @staticmethod
    def insert_employees(list_employees: List[Employee]) -> None:
        query = """
            INSERT INTO `employee` (full_name, birthday, gender)
            VALUES (?, ?, ?)
        """
        val = [(employee.full_name, employee.birthday, employee.gender.value) for employee in list_employees]
        
        DatabaseEmployee.cursor.executemany(query, val)
        DatabaseEmployee.connection.commit()


    @staticmethod
    def select_unique_employees() -> List[Employee]:
        query = """
            SELECT DISTINCT * FROM `employee`
            ORDER BY full_name
        """

        list_employees: List[Employee] = []
        database_entries = DatabaseEmployee.cursor.execute(query).fetchall()
        
        for entry in database_entries:
            full_name, birthday, gender = entry[1], convert_to_date(entry[2]), entry[3]
            list_employees.append(Employee(full_name, birthday, gender))
        
        return list_employees
    

    @staticmethod
    def select_male_employees_with_last_name_f() -> List[Employee]:
        query = """
            SELECT * FROM `employee`
            WHERE gender = 'male' AND full_name LIKE '% F% %'
            """
        
        list_employees: List[Employee] = []
        database_entries = DatabaseEmployee.cursor.execute(query).fetchall()

        for entry in database_entries:
            full_name, birthday, gender = entry[1], convert_to_date(entry[2]), entry[3]
            list_employees.append(Employee(full_name, birthday, gender))

        return list_employees
    