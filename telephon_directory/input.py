# ПолучаЮ данные от пользователя

def database ():
    base = []
    surname = input('Введите фамилию: ')
    base.append(surname)
    name = input('Введите имя: ')
    base.append(name)
    phone_number = input('Введите номер телефона: ')
    base.append(phone_number)
    comment = input('Комментарий: ')
    base.append(comment)
    return base