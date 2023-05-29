import os
import uuid


class FileService:
    def __init__(self):
        if not os.path.exists('file_storage'):
            os.makedirs('file_storage')

    def save_file(self, file_path):
        file_id = 'Такого файла не существует!'
        if os.path.isfile(file_path):
            file_id = str(uuid.uuid4())
            new_file_path = os.path.join('file_storage', file_id)
            with open(file_path, 'rb') as f:
                with open(new_file_path, 'wb') as new_f:
                    data = f.read()
                    new_f.write(data)
        print(file_id)
        return file_id

    def get_file_by_id(self, file_id):
        file_path = os.path.join(os.path.dirname(os.path.abspath(file_id)), 'file_storage', file_id)
        if os.path.exists(file_path):
            print(file_path)
        else:
            print('Такого файла нет!')
        return file_path if os.path.exists(file_path) else 'Такого файла нет!'

    def delete_file(self, file_id):
        res = 'Такого файла не существует!'
        if os.path.dirname(os.path.abspath(file_id)):
            file_path = os.path.join('file_storage', file_id)
            if os.path.exists(file_path):
                os.remove(file_path)
                res = 'Файл удален!'
        print(res)

    def change_file_id(self, old_file_id, new_file_id):
        res = 'Такого файла не существует!'
        if os.path.dirname(os.path.abspath(old_file_id)):
            old_file_path = os.path.join('file_storage', old_file_id)
            new_file_path = os.path.join('file_storage', new_file_id)
            if os.path.exists(old_file_path):
                os.rename(old_file_path, new_file_path)
                res = 'Файл изменен!'
        print(res)

    def get_files_by_ids(self, file_ids):
        result = []
        for file_id in file_ids:
            file_path = os.path.join(os.path.dirname(os.path.abspath(file_id)), 'file_storage', file_id)
            if os.path.exists(file_path):
                result.append(file_path)
            else:
                print('Такого файла нет! - ', file_id)
        print(result)
        return result

    def get_all_files(self):
        result = []
        for file_id in os.listdir('file_storage'):
            file_path = os.path.join(os.path.dirname(os.path.abspath(file_id)), 'file_storage', file_id)
            result.append({'file_id': file_id, 'file_path': file_path})
        print(result)
        return result


userAct = int(input('Введите число: '
          '\n1 - Сохранение файла по уникальному идентификатору, '
          '\n2 - Выдача сохраненного файла по идентификатору, '
          '\n3 - Удаление файла по идентификатору, '
          '\n4 - Изменение идентификатора сохраненного файла, '
          '\n5 - Получение списка файлов по нескольким идентификаторам, '
          '\n6 - Получение списка всех файлов'
          '\nВаше число: '))

file_service = FileService()
if userAct == 1:
    print('Вы выбрали действие 1 - Сохранение файла по уникальному идентификатору')
    file_id = str(input('Введите полный путь до файла: '))
    file_service.save_file(file_id)
#    '/Users/aleksandrbirukov/Desktop/1 - Файлы/вуз питон/ЯП/test.txt'
elif userAct == 2:
    print('Вы выбрали действие 2 - Выдача сохраненного файла по идентификатору')
    file_id = str(input('Введите идентификатор файла: '))
    file_service.get_file_by_id(file_id)
elif userAct == 3:
    print('Вы выбрали действие 3 - Удаление файла по идентификатору')
    file_id = str(input('Введите идентификатор файла: '))
    file_service.delete_file(file_id)
elif userAct == 4:
    print('Вы выбрали действие 4 - Изменение идентификатора сохраненного файла')
    old_file_id = str(input('Введите старый идентификатор файла: '))
    new_file_id = str(input('Введите новый идентификатор файла: '))
    file_service.change_file_id(old_file_id, new_file_id)
elif userAct == 5:
    print('Вы выбрали действие 5 - Получение списка файлов по нескольким идентификаторам')
    file_ids = ['b4ebd8db-413c-4e71-9fc5-5c452a2b3c20',
                'b5650dc9-08cc-4d13-90c1-4131c8c67d03',
                'b5650dc9-08cc-4d13-90c1-4131c8c67d',
                '9f6ef426-d94c-4c3f-af5e-529aebb46ea8']
    file_paths = file_service.get_files_by_ids(file_ids)

elif userAct == 6:
    print('Вы выбрали действие 6 - Получение списка всех файлов')
    all_files = file_service.get_all_files()
else:
    print('Вы ввели не цифру или цифру не равной ни одной из 1-6')