# Создаем файл с данными

def creat_csv():
    file = 'file.csv'
    with open ('file.txt', 'w', encoding = 'utf-8') as d:
        d.write(f'Фамилия, Имя, Телефон, Комментарий\n')