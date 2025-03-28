from requests import get, post

# print(get('http://localhost:5000/api/v2/users').json()) # получение всех ользователей
print(get('http://localhost:5000/api/v2/users/5').json()) # получение одного существующего в бд пользователя
# print(get('http://localhost:5000/api/v2/users/12').json()) # неверный id
# print(get('http://localhost:5000/api/v2/users/ffff').json()) # id = строка

print(post('http://localhost:5000/api/v2/users',
           json={'surname': 'maya',
                 'name': 'cherneckaya',
                 'age': 999,
                 'email': '1580@ya.ru',
                 'hashed_password': 'vsem2'
                 }).json())

