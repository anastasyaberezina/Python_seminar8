# Считывание данных. Запись данных.

def read_file(file):
    with open ('file.cvs', 'r', encoding='utf-8') as f:
        data = f.read()
        return data

def write_file(file, text):
    with open ('file.cvs', 'w', encoding='utf-8') as f:
        f.write(text)

