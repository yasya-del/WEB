from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    # app.run()
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    user1 = User()
    user1.surname = "Braun"
    user1.name = "Alla"
    user1.age = 25
    user1.position = "pilot"
    user1.speciality = "pilot"
    user1.address = "module_2"
    user1.email = "bra_al@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user1)
    db_sess.commit()
    user2 = User()
    user2.surname = "Uic"
    user2.name = "Jon"
    user2.age = 40
    user2.position = "ctrateg"
    user2.speciality = "scientist"
    user2.address = "module_3"
    user2.email = "j_uic@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user2)
    db_sess.commit()
if __name__ == '__main__':
    main()