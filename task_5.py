from datetime import datetime


def person_date(months):
    match int(months.month):

        case 1:
            return print(f"Вы родились в {months.year} году, {months.day} Января.")
        case 2:
            return print(f"Вы родились в {months.year} году, {months.day} Февраля.")
        case 3:
            return print(f"Вы родились в {months.year} году, {months.day} Марта.")
        case 4:
            return print(f"Вы родились в {months.year} году, {months.day} Апреля.")
        case 5:
            return print(f"Вы родились в {months.year} году, {months.day} Мая.")
        case 6:
            return print(f"Вы родились в {months.year} году, {months.day} Июня.")
        case 7:
            return print(f"Вы родились в {months.year} году, {months.day} Июля.")
        case 8:
            return print(f"Вы родились в {months.year} году, {months.day} Августа.")
        case 9:
            return print(f"Вы родились в {months.year} году, {months.day} Сентября.")
        case 10:
            return print(f"Вы родились в {months.year} году, {months.day} Октября.")
        case 11:
            return print(f"Вы родились в {months.year} году, {months.day} Ноября.")
        case 12:
            return print(f"Вы родились в {months.year} году, {months.day} Декабря.")


def personborn():
    person = input("Введите вашу дату рождение в формате ДД/ММ/ГГГГ\n")
    birthday = datetime.strptime(person, '%d/%m/%Y').date()

    (person_date(birthday))


personborn()
