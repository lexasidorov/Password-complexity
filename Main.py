from re import findall
import json

def validate_password(password):
    score = 0
    rules = ['^.{8,}$',r'[A-ZА-ЯЁ]',r'[a-zа-яё]','\d+','[!£$%&]+']
    for item in rules:
        if findall(item,password):
            score+=1
    return score


def json_users_read():
    with open('users.json','r') as f:
        users_json = f.read() # creates json obj from file
        users = json.loads(users_json) # creates list from json obj
    return users

def json_user_write(to_json):
    with open('users.json','w') as f:
        json.dump(to_json, f) # writes json obj to json file

def find_user(user):
    users = json_users_read()['users'] #creates list of users
    for item in users:
        if item['user'] == user:
            return users.index(item) # returns None if no user is found


while True:
    answer = input("Меню:\n1) Добавить пользователя\n2) Изменить пароль\n3) Вывести пользователей\n4) Выход\n--->")
    if answer == '1':
        while True:
            name = input('Введите имя пользователя:\n')
            if find_user(name) != None:
                print('Пользователь с таким именем уже существует. Попробуйте ещё раз!')
            else:
                break
        while True:
            password = input('Введите пароль:\n')
            if validate_password(password) <= 2:
                print('Этот пароль слишком слабый. Попробуйте ещё раз!')
            else:
                break
        users = json_users_read()['users']# creates list of {users}
        users.append({'user': name,'password': password})
        json_user_write({'users': users})
        print('Пользователь добавлен.')

    elif answer == '2':
        while True:
            name = input('Введите имя пользователя:\n')
            if not find_user(name):
                print('Пользователь с таким именем не существует. Попробуйте ещё раз!')
            else:
                break
        while True:
            new_password = input('Введите пароль:\n')
            if validate_password(new_password) <= 2:
                print('Этот пароль слишком слабый. Попробуйте ещё раз!')
            else:
                break
        users = json_users_read()['users']# creates list of {users}
        users[find_user(name)]['password'] = new_password
        json_user_write({'users':users})
        print('Пароль изменён.')

    elif answer == '3':
        print('Пользователи:\n','\n'.join(i.get('user') for i in json_users_read()['users'])) # shows values ander 'user' keys from list of dicts

    elif answer == '4':
        print('До свидания!')
        break
    else:
        print('Некорректный ввод!')