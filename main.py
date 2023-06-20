from flask import Flask, render_template, request, g, session
import datetime
import os
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

# ______________________________________________________________________________________________________________________


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ffghjkmcxdertyuio76543wedcfjio9rdfcvbtghu7fdsw45tfdr'
DATABASE = '/main.db'
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'main.db')))
# подключение БД в проект
app.permanent_session_lifetime = datetime.timedelta(days=40)


# ______________________________________________________________________________________________________________________


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


# ______________________________________________________________________________________________________________________


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    # ......................................................................................................................

    @property
    def getMenu(self):
        sql = '''SELECT * FROM tovar'''

        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res

        except:

            print("Ошибка чтения из БД")
        return []

    # ......................................................................................................................

    def regUser(self, name, tel, address, pasw):
        sql = f"INSERT INTO user VALUES (NULL, ?, ?, ?, ?);"

        try:
            self.__cur.execute(f"SELECT COUNT() as `count` FROM user WHERE phone LIKE '{tel}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Пользователь с таким email уже существует")
                return False
            else:
                self.__cur.executemany(sql, [(name, tel, address, generate_password_hash(pasw))])
                self.__db.commit()
                return True

        except:
            print("Ошибка добавления пользователя")

    # ......................................................................................................................

    def get_user_id(self, phone):
        sql = f'''SELECT * FROM user WHERE phone == "{phone}" '''

        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
            else:
                return []
        except:
            print("Ошибка чтения из БД id пользователя")

    # ......................................................................................................................

    def add_tovar(self, id1, id_user):
        sql = f'''SELECT * FROM tovar WHERE id == "{id1}" '''
        sql2 = f'''INSERT INTO added_by_user VALUES (?, ?, ?, ?);'''
        sql3 = f'''SELECT * FROM added_by_user WHERE id_tovar == "{id1}" AND id_user == "{id_user}" '''

        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()

            self.__cur.execute(sql3)
            res2 = self.__cur.fetchall()

            if not res2:
                self.__cur.executemany(sql2, [(id_user, res[0][0], res[0][2], 1)])
                self.__db.commit()

        except:
            print("Ошибка добавления товара в карзину")

    # ......................................................................................................................

    def get_cor(self, id2):
        sql = f'''SELECT * FROM added_by_user WHERE id_user == "{id2}" '''

        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            id_tov = []

            for i in res:
                id_tov.append([i[1], i[3]])

            inf_tovar = []
            tovar = []

            for i in id_tov:
                self.__cur.execute(f'''SELECT * FROM tovar WHERE id == "{i[0]}" ''')
                res = self.__cur.fetchall()
                inf_tovar.append(res[0])
                inf_tovar.append(i[1])
                tovar.append(inf_tovar)
                inf_tovar = []

            if tovar: return tovar

        except:

            print("Ошибка")
        return []

    # ......................................................................................................................

    def delete_tovar(self, id_user, id_tovar):
        sql = f'DELETE FROM added_by_user WHERE id_user = "{id_user}" AND id_tovar == "{id_tovar}";'
        print("dellllllllllllllllll")
        try:
            self.__cur.execute(sql)
            self.__db.commit()
        except:
            print("Ошибка удоления")

    # ......................................................................................................................

    def get_delivery(self, id2):
        sql = f'SELECT * FROM added_by_user WHERE id_user == "{id2}";'
        sql2 = f'INSERT INTO delivery VALUES (?, ?, NULL, ?);'
        sql3 = f'INSERT INTO coll_delivery VALUES (?);'
        sql4 = f'SELECT * FROM coll_delivery WHERE id_user == "{id2}";'
        sql5 = f'DELETE FROM added_by_user WHERE id_user == "{id2}";'

        try:
            self.__cur.execute(sql)
            data = self.__cur.fetchall()
            for i in data:
                self.__cur.execute(f'SELECT * FROM delivery WHERE id_tovara == "{i[1]}" AND id_user == "{id2}" ')
                qwe = self.__cur.fetchall()
                if not qwe:
                    self.__cur.executemany(sql2, [(i[1], i[0], i[3])])
                    print(i[3])
            self.__db.commit()

            self.__cur.execute(sql4)
            data = self.__cur.fetchall()
            print(data)
            if not data:
                self.__cur.execute(sql3, [id2])
            self.__db.commit()

            self.__cur.execute(sql5)
            self.__db.commit()
        except:
            print('Ошибка добавления в доставку')

    # ......................................................................................................................

    def add_quanitiy(self, quantity, id_tovar, id_user):
        sql = f'UPDATE added_by_user SET quantity = {quantity} WHERE id_tovar == {id_tovar} AND id_user == {id_user};'

        try:
            self.__cur.execute(sql)
            self.__db.commit()
        except:
            print("Ошибка добавления колличества товаров")

    # ......................................................................................................................

    def get_tovars_for_index(self):
        sql = f'SELECT * FROM for_index'

        try:
            self.__cur.execute(sql)
            ids = self.__cur.fetchall()

            retu = []

            for i in ids:
                self.__cur.execute(f'SELECT * FROM tovar WHERE id == {i[0]}')
                ret = self.__cur.fetchall()
                a = [ret[0], i[1]]
                if ret:
                    retu.append(a)
            return retu

        except:
            print("Ошибка вывода на главную страницу")

    # ......................................................................................................................

    def get_deliveri(self, id2):
        sql = f'''SELECT * FROM delivery WHERE id_user == "{id2}" '''

        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            id_tov = []

            for i in res:
                id_tov.append([i[0], i[3], i[2]])

            inf_tovar = []
            tovar = []

            for i in id_tov:
                self.__cur.execute(f'''SELECT * FROM tovar WHERE id == "{i[0]}" ''')
                res = self.__cur.fetchall()
                inf_tovar.append(res[0])
                inf_tovar.append(i[1])
                inf_tovar.append(i[2])
                tovar.append(inf_tovar)
                inf_tovar = []

            if tovar: return tovar

        except:

            print("Ошибка")
        return []


# ______________________________________________________________________________________________________________________


def get_db():
    # Соединение с БД, если оно еще не установлено
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


# ______________________________________________________________________________________________________________________


@app.route("/", methods=["POST", "GET"])
def index():
    db = get_db()
    conn = FDataBase(db)
    a = conn.get_tovars_for_index()

    d = len(a)
    d = d // 3
    d = int(d)

    if request.method == "POST":
        todo = request.form.get("todo")
        print(todo)
        if 'authorization' in session:
            db = get_db()
            asd = FDataBase(db)
            s = session['authorization']
            asd.add_tovar(todo, s)
        else:
            print("зарегестрируйтесь")

    if 'authorization' in session:
        return render_template("index.html", tov=a, d=d)

    else:
        return render_template("index_no_avtor.html", tov=a, d=d)


# ......................................................................................................................


@app.route("/reg", methods=["POST", "GET"])
def reg():
    if 'authorization' in session:
        db = get_db()
        conn = FDataBase(db)
        a = conn.get_deliveri(session['authorization'])

        return render_template("deliveri.html", tov=a)

    else:
        if request.method == "POST":
            print(request.form)
            db = get_db()
            conn = FDataBase(db)

            inf = conn.get_user_id(request.form['nic'])  # получение информации из базы данных по номеру телефона

            if inf:  # проверка на наличие данных
                id = inf[0][0]  # получение id
                parol = inf[0][4]  # получение пароля
                print(id)
                print(parol)
                if check_password_hash(parol,
                                       request.form['pas']):  # сравнивание паролей на савподение через хеширование
                    session.permanent = True
                    session['authorization'] = id
                    print("_______________________________")
                else:
                    print("Неправельный пароль")
        return render_template("reg.html")


# ......................................................................................................................


@app.route("/reg_reg", methods=["POST", "GET"])
def reg_reg():
    if request.method == "POST":
        print(request.form)

        if request.form['pas1'] == request.form['pas2']:
            db = get_db()
            conn = FDataBase(db)
            a = conn.regUser(request.form['nic'], request.form['namber'], request.form['adres'], request.form['pas1'])
            # запись информации из формы в БД ^^^^^^^^^^^^^^^^^^^^^ "а" возврашает есть ли такой же номер в бд
            if a and check_password_hash(conn.get_user_id(request.form['namber'])[0][4], request.form['pas1']):
                # запись в сесии уникального индификатора если такой номер уже есть и пароли совпадают с введенным
                b = conn.get_user_id(request.form['namber'])
                session.permanent = True
                session['authorization'] = b[0][0]
                print(session['authorization'])

        else:
            print("проли не совпали")

    return render_template("reg_reg.html")


# ......................................................................................................................


@app.route("/menu", methods=["POST", "GET"])
def menu():
    if request.method == "POST":
        todo = request.form.get("todo")
        if 'authorization' in session:
            db = get_db()
            asd = FDataBase(db)
            s = session['authorization']
            asd.add_tovar(todo, s)
        else:
            print("зарегестрируйтесь")

    db = get_db()
    asd = FDataBase(db)

    if 'authorization' in session:
        return render_template("menu.html", tov=asd.getMenu)

    else:
        return render_template("menu_no_avtorization.html", tov=asd.getMenu)


# ......................................................................................................................


@app.teardown_appcontext
def close_db(error):
    # Закрываем соединение с БД, если оно было установлено
    if hasattr(g, 'link_db'):
        g.link_db.close()


# ......................................................................................................................


@app.route("/cor", methods=["POST", "GET"])
@app.route("/cor/<int:id_tova>", methods=["POST", "GET"])
def cor(id_tova=-1):
    db = get_db()
    asd = FDataBase(db)

    if request.method == "POST":
        print(1)

        a = asd.get_cor(session['authorization'])
        for i in a:
            a = i[0][0]
            a = str(a)
            b = request.form.get(f"asd{a}")
            print(b)
            print(2)

            if b is not None:
                print(3)
                asd.add_quanitiy(b, i[0][0], session['authorization'])

        asd.get_delivery(session['authorization'])
    print("id ", id_tova)
    if id_tova != -1:
        print(4)
        print(id_tova)
        asd.delete_tovar(session['authorization'], id_tova)

    if 'authorization' in session:
        print(5)
        a = asd.get_cor(session['authorization'])
    else:
        print("авторизируйтесь")
        a = []

    vh = 'Вход'
    if 'authorization' in session:
        vh = 'Доставка'

    return render_template("cor.html", tov=a, vh=vh)


# ......................................................................................................................


@app.route("/conta")
def conta():
    vh = 'Вход'
    if 'authorization' in session:
        vh = 'Доставка'
    return render_template("conta.html", vh=vh)


# ......................................................................................................................


@app.route("/del")
def del_s():
    session.clear()
    db = get_db()
    asd = FDataBase(db)
    return render_template("menu.html", tov=asd.getMenu)


# ______________________________________________________________________________________________________________________


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
