import argparse
from src.queries import DatabaseEmployee
from src.employee import Employee, Gender, generate_random_employees, generate_employees_witch_F
from src import utils
import time


def createParser():
    parser = argparse.ArgumentParser(description="Программа для учета сотрудников")
    subparsers = parser.add_subparsers(dest="script", help="Выберите скрипт")

    subparsers.add_parser("1", help="Создание базы данных.")
    
    parser_2 = subparsers.add_parser("2", help="Внести сотрудника в базу данных")
    parser_2.add_argument("full_name", type=str, help="ФИО сотрудника")
    parser_2.add_argument("birthday", type=str, help="День рождения (В формате ГГГГ.ММ.ДД)")
    parser_2.add_argument("gender", type=str, help="Половая принадлежность (male/female)")
    
    subparsers.add_parser("3", help="Показать всех сотрудников")

    parser_4 = subparsers.add_parser("4", help="Сгенерировать N сотрудников и записать в базу данных")
    parser_4.add_argument("amount", type=int, help="Количество сотрудников")

    subparsers.add_parser("5", help="Показать сотрудников мужчин с фамилией на 'F'")

    return parser


def main() -> None:
    parser = createParser()
    args = parser.parse_args()

    match args.script:
        case "1":
            DatabaseEmployee.create_table()
            print("База данных создана.")

        case "2":
            birthday = utils.convert_to_date(args.birthday)
            if birthday == None: return
            if args.gender not in Gender:
                print("Гендер указан неверно.")
                return
            
            employee = Employee(args.full_name, birthday, Gender(args.gender))
            DatabaseEmployee.insert_employees([employee])

            print("Сотрудник добавлен")

        case "3":
            list_employees = DatabaseEmployee.select_unique_employees()
            for employee in list_employees:
                print("{0} {1} {2} возраст: {3} года.".format(employee.full_name, employee.birthday, employee.gender, employee.calculate_age()))

        case "4":
            list_employees = generate_random_employees(args.amount)
            DatabaseEmployee.insert_employees(list_employees)

            list_employees_last_name_F = generate_employees_witch_F(100)
            DatabaseEmployee.insert_employees(list_employees_last_name_F)

            print("Сотрудники добавлены.")

        case "5":
            start_time = time.time()

            list_employees = DatabaseEmployee.select_male_employees_with_last_name_f()
            print(f"Количество мужчин с фамилией на 'F': {len(list_employees)}")
            
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Время выполнения: {round(execution_time, 6)}c.")



    DatabaseEmployee.connection.close()


if __name__ == "__main__":
    main()