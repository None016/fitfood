import aiogram as ai
import logging
import sqlite3 as sq
import datetime

# ______________________________________________PROGRAM_VARIABLE________________________________________________________

data_admins = [None, None, None, None]
data_key = [0, 0, 0, 0]
key_code = 0
given_user = {}
coll_centr = {}

# ______________________________________________SETTINGS_AIOGRAM________________________________________________________

bot = ai.Bot(token='5964735418:AAED-s-7mmcK7x5AD2rRjjjRUbFZloHC78g')
fit = ai.Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


# _________________________________________________KEYBOARD_LEVAL_0__________________________________________________________


bt20 = ai.types.KeyboardButton("📞Начать обзвон покупателей📞")

bt1 = ai.types.KeyboardButton('👤Добавить работника👤')
bt2 = ai.types.KeyboardButton('👤❌Удалить работника❌👤')
bt2_1 = ai.types.KeyboardButton('Добавить товар🖋')
klav0 = ai.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

klav0.row(bt2_1)
klav0.row(bt20)
klav0.row(bt1)
klav0.row(bt2)


# ________________________________________________INLINE_KEYBOARD_1_____________________________________________________


bt3 = ai.types.InlineKeyboardButton('Имя', callback_data='button1')
bt4 = ai.types.InlineKeyboardButton('Уровень доступа', callback_data='button2')
bt5 = ai.types.InlineKeyboardButton('Должность', callback_data='button3')
bt6 = ai.types.InlineKeyboardButton('ID', callback_data='button4')
bt7 = ai.types.InlineKeyboardButton('Добавть', callback_data='button5')
bt8 = ai.types.InlineKeyboardButton('Отмена', callback_data='button6')
klav0_1 = ai.types.InlineKeyboardMarkup()
klav0_1.row(bt3, bt4)
klav0_1.row(bt5, bt6)
klav0_1.row(bt8)
klav0_1.row(bt7)


# _________________________________________________INLINE_KEYBOARD_2____________________________________________________


bt8 = ai.types.InlineKeyboardButton('Название товара', callback_data='button7')
bt9 = ai.types.InlineKeyboardButton('Цена', callback_data='button8')
bt10 = ai.types.InlineKeyboardButton('Белки', callback_data='button9')
bt11 = ai.types.InlineKeyboardButton('Жиры', callback_data='button10')
bt12 = ai.types.InlineKeyboardButton('Углеводы', callback_data='button11')
bt13 = ai.types.InlineKeyboardButton('Колории', callback_data='button12')
bt14 = ai.types.InlineKeyboardButton('Описание', callback_data='button13')
bt15 = ai.types.InlineKeyboardButton('Отправить', callback_data='button14')
bt16 = ai.types.InlineKeyboardButton('Оменить', callback_data='button15')
bt17 = ai.types.InlineKeyboardButton('Добавить обложку товара', callback_data='button16')
bt18 = ai.types.InlineKeyboardButton('Добавить фото товара', callback_data='button17')

klav1_1 = ai.types.InlineKeyboardMarkup()
klav1_1.row(bt8)
klav1_1.row(bt10, bt11, bt12)
klav1_1.row(bt13)
klav1_1.row(bt14, bt9)
klav1_1.row(bt17)
klav1_1.row(bt18)
klav1_1.row(bt15, bt16)


# ________________________________________________KEYBOARD_LEVAL_1______________________________________________________


bt20 = ai.types.KeyboardButton("📞Начать обзвон покупателей📞")

klav1 = ai.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

klav1.row(bt2_1)
klav1.row(bt20)


# ________________________________________________INLINE_KEYBOARD_3_____________________________________________________


bt21 = ai.types.InlineKeyboardButton("Следующий", callback_data="button20")
bt22 = ai.types.InlineKeyboardButton("Позвонил", callback_data="button21")
bt23 = ai.types.InlineKeyboardButton("Завершить обзвон", callback_data="button22")
bt24 = ai.types.InlineKeyboardButton("Доавить время заказа", callback_data="button23")
bt25 = ai.types.InlineKeyboardButton("Добавить позицию", callback_data="button24")
bt26 = ai.types.InlineKeyboardButton("Удалить позицию", callback_data="button30")

klav1_2 = ai.types.InlineKeyboardMarkup()
klav1_3 = ai.types.InlineKeyboardMarkup()
klav1_4 = ai.types.InlineKeyboardMarkup()

klav1_3.row(bt21)
klav1_3.row(bt23)

klav1_4.row(bt25)
klav1_4.row(bt26)
klav1_4.row(bt24)
klav1_4.row(bt22)


# _________________________________________________INLINE_KEYBOARD_4____________________________________________________


bt26 = ai.types.InlineKeyboardButton("ID товара", callback_data="button25")
bt28 = ai.types.InlineKeyboardButton("Время", callback_data="button27")
bt29 = ai.types.InlineKeyboardButton("Колличество", callback_data="button28")
bt30 = ai.types.InlineKeyboardButton("Отправить", callback_data="button29")

klav1_5 = ai.types.InlineKeyboardMarkup()

klav1_5.row(bt26)
klav1_5.row(bt28)
klav1_5.row(bt29)
klav1_5.row(bt30)


# ____________________________________________WORKING_WITH_THE_DATABASE_________________________________________________


class db_connect:
    def __init__(self, which_db):
        self.sql = None
        self.cur = None
        try:
            self.sql = sq.connect(which_db)
            self.cur = self.sql.cursor()
        except:
            print("ошибка подключения базы данных")

    def select(self, table, which_column, id1):
        sql = f'SELECT * FROM {table} WHERE {which_column} == "{id1}"'
        try:
            self.cur.execute(sql)
            data = self.cur.fetchall()
            return data
        except:
            print('Ошибка получения id')

    def add_admin(self, name, level, jo_title, id1):
        sql = f'INSERT INTO admins_and_privilege VALUES (?, ?, ?, NULL, ?);'
        try:
            self.cur.executemany(sql, [(name, level, jo_title, id1)])
            self.sql.commit()
        except:
            print('Ошибка добавления пользователья')

    def del_line(self, table, column, id1):
        sql = f'DELETE FROM {table} WHERE {column} == {id1}'
        try:
            self.cur.execute(sql)
            self.sql.commit()
        except:
            print('Ошибка удаления пользователей')

    def add_product(self, tovar, prise, bel, zir, colors, opis, ygl, p1, p2, id1):
        sql = f'INSERT INTO tovar VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'
        try:
            self.cur.executemany(sql, [(tovar, prise, bel, zir, colors, ygl, p1, opis, p2, id1)])
            self.sql.commit()
        except:
            print('Ошибка добавления пользователья')

    def add_tovars(self, id_tovar, id_user, time, quantity):
        sql = 'INSERT INTO delivery VALUES (?, ?, ?, ?) '
        try:
            a = self.select('tovar', 'id', id_tovar)
            b = self.select('user', 'id', id_user)

            if a and b:
                self.cur.executemany(sql, [(id_tovar, id_user, time, quantity)])
                self.sql.commit()
        except:
            print('Ошибка добавления товара')

    def select_not_where(self, table):
        sql = f"SELECT * FROM {table};"
        try:
            self.cur.execute(sql)
            dat = self.cur.fetchall()
            return dat
        except:
            print("Ошибка получения двнных из табоицы")

    def update(self, tabel, col_update, data_update, line, data_line):
        sql = f'UPDATE {tabel} SET {col_update} = "{data_update}" WHERE {line} == {data_line};'
        try:
            self.cur.execute(sql)
            self.sql.commit()
        except:
            print("Ошибка обнавелия таблицы")

    def delete(self, table, select):
        sql = f'DELETE FROM {table} WHERE {select}'
        try:
            self.cur.execute(sql)
            self.sql.commit()
        except: print("Ошибка удаления")


# _________________________________________________SECONDARY_FUNCTIONS__________________________________________________


def add_memori(id1):
    if not(f"{id1}" in given_user.keys()):
        given_user[f"{id1}"] = [[None, None, None, None, None, None, None, None, None, id1], 0]


def dataus(id1):
    d = given_user[f'{id1}'][0]
    return f'''
Название: {d[0]}
Цена: {d[1]}
Колличество белков: {d[2]}
Колличество жиров: {d[3]}
Колличество угливодов: {d[4]}
Колличество Коллорий: {d[5]}
Описание: {d[6]}
Обложка товара: {d[7]}
Фотография товара: {d[8]} 
Ваш id {d[9]}   
'''


# ________________________________________________EVENT_HANDLING________________________________________________________


@fit.message_handler(commands=['start'])
async def start(sms: ai.types.Message):
    sq = db_connect('fitFoot_db.db')
    data = sq.select('admins_and_privilege', 'id', sms.from_id)
    if data:
        if data[0][1] == 0:
            add_memori(sms.from_id)
            await sms.answer(f"Привет {data[0][0]}", reply_markup=klav0)
        elif data[0][1] == 1:
            add_memori(sms.from_id)
            await sms.answer(f"Привет {data[0][0]}", reply_markup=klav1)

    else:
        await sms.answer(f"Привет")


# _______________________________________________PROCESSING_SENT_TEXT___________________________________________________


@fit.message_handler(content_types=['text', 'photo'])
async def text_mesage(sms: ai.types.Message):
    global key_code
    sq = db_connect('fitFoot_db.db')
    data = sq.select('admins_and_privilege', 'id', sms.from_id)
    print(given_user)

    if f"{sms.chat.id}" in coll_centr.keys():
        if coll_centr[f"{sms.chat.id}"] and coll_centr[f"{sms.chat.id}"][0][1] == -1:
            coll_centr[f'{sms.chat.id}'][1] = 0
            db = db_connect('main.db')
            db.update('delivery', 'time', f'{sms.text}', 'id_user', coll_centr[f"{sms.chat.id}"][0][0])
            await bot.send_message(sms.chat.id, 'Время добавленно')
        elif coll_centr[f"{sms.chat.id}"] and coll_centr[f"{sms.chat.id}"][2] == 1:
            coll_centr[f"{sms.chat.id}"][1][0] = sms.text
            coll_centr[f"{sms.chat.id}"][2] = 0
            await bot.delete_message(sms.chat.id, sms.message_id)
            await bot.delete_message(sms.chat.id, sms.message_id - 1)
            print(coll_centr)
        elif coll_centr[f"{sms.chat.id}"] and coll_centr[f"{sms.chat.id}"][2] == 2:
            coll_centr[f"{sms.chat.id}"][1][1] = sms.text
            coll_centr[f"{sms.chat.id}"][2] = 0
            await bot.delete_message(sms.chat.id, sms.message_id)
            await bot.delete_message(sms.chat.id, sms.message_id - 1)
            print(coll_centr)
        elif coll_centr[f"{sms.chat.id}"] and coll_centr[f"{sms.chat.id}"][2] == 3:
            coll_centr[f"{sms.chat.id}"][1][2] = sms.text
            coll_centr[f"{sms.chat.id}"][2] = 0
            await bot.delete_message(sms.chat.id, sms.message_id)
            await bot.delete_message(sms.chat.id, sms.message_id - 1)
            print(coll_centr)
        elif coll_centr[f"{sms.chat.id}"] and coll_centr[f"{sms.chat.id}"][2] == 4:
            coll_centr[f"{sms.chat.id}"][1][3] = sms.text
            coll_centr[f"{sms.chat.id}"][2] = 0
            await bot.delete_message(sms.chat.id, sms.message_id)
            await bot.delete_message(sms.chat.id, sms.message_id - 1)
            print(coll_centr)
        elif coll_centr[f"{sms.chat.id}"] and coll_centr[f"{sms.chat.id}"][2] == 5:
            coll_centr[f"{sms.chat.id}"][2] = 0
            dob_db = db_connect('main.db')
            dob_db.delete('delivery', f'id_tovara == "{sms.text}" AND id_user == "{coll_centr[f"{sms.chat.id}"][0][0]}"')

            await bot.delete_message(sms.chat.id, sms.message_id)
            await bot.delete_message(sms.chat.id, sms.message_id - 1)
            await bot.delete_message(sms.chat.id, sms.message_id - 2)

            db = db_connect("main.db")
            a = coll_centr[f"{sms.from_user.id}"][1]
            db.add_tovars(a[0], coll_centr[f"{sms.from_user.id}"][0][0], a[2], a[3])

            b = db.select('delivery', 'id_user', coll_centr[f"{sms.from_user.id}"][0][0])
            print(b)

            c = db.select('user', 'id', coll_centr[f"{sms.from_user.id}"][0][0])
            print(c)
            db.del_line('coll_delivery', 'id_user', coll_centr[f"{sms.from_user.id}"][0][0])

            await bot.send_message(sms.from_user.id,
                                   f'Имя: {c[0][1]} \nТелефон: {c[0][2]} \nАдрес: {c[0][3]} \n \n {tov(b, db)}',
                                   reply_markup=klav1_4)

            print(coll_centr)

    if data:
        if data[0][1] == 0 and sms.text == '👤Добавить работника👤':
            await bot.send_message(sms.from_id, f"Выберите что добавть", reply_markup=klav0_1)
        elif data[0][1] <= 1 and sms.text == 'Добавить товар🖋':
            add_memori(sms.from_id)
            print(given_user[f"{sms.from_id}"])
            await bot.send_message(sms.from_id, f"Выберите поле для добавления товара", reply_markup=klav1_1)

        elif data[0][1] <= 1 and sms.text == "📞Начать обзвон покупателей📞":
            coll_centr[f'{sms.chat.id}'] = [[None, 0], [None, None, None, None], 0]
            await bot.send_message(sms.chat.id, f"Обзвон начат", reply_markup=klav1_3)


# _______________________________________________EDITING_ADD_AN_ADMIN___________________________________________________

        elif data[0][1] == 0 and data_key[0] == 1:
            print(sms.text)
            data_admins[0] = sms.text
            data_key[0] = 0
            await bot.send_message(sms.from_id, f"{data_admins}", reply_markup=klav0_1)
        elif data[0][1] == 0 and data_key[1] == 1:
            data_admins[1] = sms.text
            data_key[1] = 0
            await bot.send_message(sms.from_id, f"{data_admins}", reply_markup=klav0_1)
        elif data[0][1] == 0 and data_key[2] == 1:
            data_admins[2] = sms.text
            data_key[2] = 0
            await bot.send_message(sms.from_id, f"{data_admins}", reply_markup=klav0_1)
        elif data[0][1] == 0 and data_key[3] == 1:
            data_admins[3] = sms.text
            data_key[3] = 0
            await bot.send_message(sms.from_id, f"{data_admins}", reply_markup=klav0_1)

        elif data[0][1] == 0 and key_code == 1:
            key_code = 0
            db = db_connect('fitFoot_db.db')
            db.del_line('admins_and_privilege', 'id', sms.text)
            await bot.send_message(sms.from_id, 'Админ удален', reply_markup=klav0)

        elif data[0][1] == 0 and sms.text == '👤❌Удалить работника❌👤':
            key_code = 1
            await bot.send_message(sms.from_id, f"Введите id работника для удаления")


# ______________________________________________________________________________________________________________________

        elif f'{sms.chat.id}' in given_user.keys():
            if data[0][1] <= 1 and given_user[f"{sms.from_user.id}"][1] == 8:
                now = datetime.datetime.now()
                given_user[f"{sms.from_user.id}"][0][7] = f'ph{sms.chat.id}{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}{now.microsecond}.png'
                await sms.photo[-1].download(f'''static\img\ph{sms.chat.id}{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}{now.microsecond}.png''')
                print(sms.message_id)
                await bot.delete_message(sms.chat.id, sms.message_id)
                await bot.delete_message(sms.chat.id, sms.message_id - 1)
                await bot.delete_message(sms.chat.id, sms.message_id - 2)
                await bot.send_message(sms.from_user.id, f'Выберите что еще добавить {dataus(sms.from_user.id)}',
                                       reply_markup=klav1_1)

            elif data[0][1] <= 1 and given_user[f"{sms.from_user.id}"][1] == 9:
                now = datetime.datetime.now()
                given_user[f"{sms.from_user.id}"][0][8] = f'ph{sms.chat.id}{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}{now.microsecond}.png'
                await sms.photo[-1].download(f'''static\img\ph{sms.chat.id}{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}{now.microsecond}.png''')
                await bot.delete_message(sms.chat.id, sms.message_id)
                await bot.delete_message(sms.chat.id, sms.message_id - 1)
                await bot.delete_message(sms.chat.id, sms.message_id - 2)
                await bot.send_message(sms.from_user.id, f'Выберите что еще добавить {dataus(sms.from_user.id)}',
                                       reply_markup=klav1_1)

            elif data[0][1] <= 1 and given_user[f"{sms.from_user.id}"][1]:
                if given_user[f"{sms.from_user.id}"][1] != 8 and given_user[f"{sms.from_user.id}"][1] != 9:
                    given_user[f"{sms.from_user.id}"][0][given_user[f"{sms.from_user.id}"][1]-1] = sms.text
                    await bot.delete_message(sms.chat.id, sms.message_id)
                    await bot.delete_message(sms.chat.id, sms.message_id - 1)
                    await bot.delete_message(sms.chat.id, sms.message_id - 2)
                    await bot.send_message(sms.from_user.id, f'Выберите что еще добавить {dataus(sms.from_user.id)}',
                                           reply_markup=klav1_1)
    else:
        await sms.answer(f"Привет")


# ________________________________________________BUTTON_PROCESSING_1___________________________________________________


@fit.callback_query_handler(text='button1')
async def button1(sms: ai.types.message):
    print(data_admins)
    data_key[0] = 1
    print(data_key)
    await bot.send_message(sms.from_user.id, 'Введите имя')


@fit.callback_query_handler(text='button2')
async def button2(sms: ai.types.message):
    print(data_admins)
    data_key[1] = 1
    print(data_key)
    await bot.send_message(sms.from_user.id, 'Введите уровень доступа')


@fit.callback_query_handler(text='button3')
async def button3(sms: ai.types.message):
    print(data_admins)
    data_key[2] = 1
    await bot.send_message(sms.from_user.id, 'Введите Должность')


@fit.callback_query_handler(text='button4')
async def button4(sms: ai.types.message):
    print(data_admins)
    data_key[3] = 1
    await bot.send_message(sms.from_user.id, 'Введите ID')


@fit.callback_query_handler(text='button5')
async def button5(sms: ai.types.message):
    print(data_admins)
    if data_admins[0] and data_admins[1] and data_admins[2] and data_admins[3]:
        db = db_connect('fitFoot_db.db')
        db.add_admin(data_admins[0], data_admins[1], data_admins[2], data_admins[3])
        for i in range(4):
            data_admins[i] = None
        print(data_admins)
        await bot.send_message(sms.from_user.id, 'Отправлено', reply_markup=klav0)


@fit.callback_query_handler(text='button6')
async def button5(sms: ai.types.message):
    for i in range(4):
        data_admins[i] = None

    data_key = [0, 0, 0, 0]
    await bot.send_message(sms.from_user.id, f'Отменено {data_admins} \n {data_key}')


# ________________________________________________BUTTON_PROCESSING_2___________________________________________________


@fit.callback_query_handler(text='button7')
async def button7(sms: ai.types.message):
    if f"{sms.from_user.id}" in given_user.keys():
        given_user[f"{sms.from_user.id}"][1] = 1
        print(given_user[f"{sms.from_user.id}"])
        await bot.send_message(sms.from_user.id, f'Введите название товара')


@fit.callback_query_handler(text='button8')
async def button8(sms: ai.types.message):
    if f"{sms.from_user.id}" in given_user.keys():
        given_user[f"{sms.from_user.id}"][1] = 2
        print(given_user[f"{sms.from_user.id}"])
        await bot.send_message(sms.from_user.id, f'Введите цену')


@fit.callback_query_handler(text='button9')
async def button9(sms: ai.types.message):
    if f"{sms.from_user.id}" in given_user.keys():
        given_user[f"{sms.from_user.id}"][1] = 3
        print(given_user[f"{sms.from_user.id}"])
        await bot.send_message(sms.from_user.id, f'Введите колличество белков')


@fit.callback_query_handler(text='button10')
async def button10(sms: ai.types.message):
    if f"{sms.from_user.id}" in given_user.keys():
        given_user[f"{sms.from_user.id}"][1] = 4
        print(given_user[f"{sms.from_user.id}"])
        await bot.send_message(sms.from_user.id, f'Введите колличество жиров')


@fit.callback_query_handler(text='button11')
async def button11(sms: ai.types.message):
    if f"{sms.from_user.id}" in given_user.keys():
        given_user[f"{sms.from_user.id}"][1] = 5
        print(given_user[f"{sms.from_user.id}"])
        await bot.send_message(sms.from_user.id, f'Введите колличество углеводов')


@fit.callback_query_handler(text='button12')
async def button12(sms: ai.types.message):
    if f"{sms.from_user.id}" in given_user.keys():
        given_user[f"{sms.from_user.id}"][1] = 6
        print(given_user[f"{sms.from_user.id}"])
        await bot.send_message(sms.from_user.id, f'Введите колличество коллорий')


@fit.callback_query_handler(text='button13')
async def button13(sms: ai.types.message):
    if f"{sms.from_user.id}" in given_user.keys():
        given_user[f"{sms.from_user.id}"][1] = 7
        print(given_user[f"{sms.from_user.id}"])
        await bot.send_message(sms.from_user.id, f'Введите описание товара')


@fit.callback_query_handler(text='button14')
async def button14(sms: ai.types.message):
    if f"{sms.from_user.id}" in given_user.keys():
        dat = given_user[f"{sms.from_user.id}"][0]
        if dat[0] and dat[1] and dat[2] and dat[3] and dat[4] and dat[5] and dat[6]:
            db = db_connect('main.db')
            db.add_product(dat[0], dat[1], dat[2], dat[3], dat[4], dat[5], dat[6], dat[7], dat[8], dat[9])
            given_user[f"{sms.from_user.id}"][1] = 0
            given_user[f"{sms.from_user.id}"][0] = [None, None, None, None, None, None, None, None, None, None]
            print(given_user[f"{sms.from_user.id}"])
            await bot.send_message(sms.from_user.id, f'Отправленно \n {given_user[f"{sms.from_user.id}"]}')
        else:
            await bot.send_message(sms.from_user.id, f'Вы ввели не все значения \n {dataus(sms.from_user.id)}')


@fit.callback_query_handler(text='button15')
async def button15(sms: ai.types.message):
    if f"{sms.from_user.id}" in given_user.keys():
        given_user[f"{sms.from_user.id}"][1] = 0
        given_user[f"{sms.from_user.id}"][0] = [None, None, None, None, None, None, None, None, None, None]
        print(given_user[f"{sms.from_user.id}"])
        await bot.send_message(sms.from_user.id, f'Отменено \n {given_user[f"{sms.from_user.id}"]}')


@fit.callback_query_handler(text='button16')
async def button16(sms: ai.types.message):
    if f"{sms.from_user.id}" in given_user.keys():
        given_user[f"{sms.from_user.id}"][1] = 8
        print(given_user[f"{sms.from_user.id}"])
        await bot.send_message(sms.from_user.id, f'Отпрвте обложку товара')


@fit.callback_query_handler(text='button17')
async def button17(sms: ai.types.message):
    if f"{sms.from_user.id}" in given_user.keys():
        given_user[f"{sms.from_user.id}"][1] = 9
        print(given_user[f"{sms.from_user.id}"])
        await bot.send_message(sms.from_user.id, f'Отправте фото товара')


# ______________________________________________________________________________________________________________________


@fit.callback_query_handler(text="button21")
async def button22(sms: ai.types.message):
    await bot.send_message(sms.from_user.id, f"Нажмите 'Следующий' когда будете готовы", reply_markup=klav1_3)


@fit.callback_query_handler(text="button20")
async def button20(sms: ai.types.message):
    db = db_connect('main.db')
    a = db.select_not_where('coll_delivery')
    if a:
        print(a[0][0])
        b = db.select('delivery', 'id_user', a[0][0])
        print(b)

        c = db.select('user', 'id', a[0][0])
        print(c)
        db.del_line('coll_delivery', 'id_user', a[0][0])

        coll_centr[f"{sms.from_user.id}"][0][0] = a[0][0]

        await bot.send_message(sms.from_user.id, f'Имя: {c[0][1]} \nТелефон: {c[0][2]} \nАдрес: {c[0][3]} \n \n {tov(b, db)}', reply_markup=klav1_4)
    else: await bot.send_message(sms.from_user.id, "На данный момент нет пользователей которым необходимо позвонить повторите операцию через минуту", reply_markup=klav1_3)


@fit.callback_query_handler(text="button22")
async def button22(sms: ai.types.message):
    await bot.send_message(sms.from_user.id, f"Вы завершили обзвон",)


@fit.callback_query_handler(text="button23")
async def button22(sms: ai.types.message):
    coll_centr[f"{sms.from_user.id}"][0][1] = -1
    await bot.send_message(sms.from_user.id, f"Введите время доставки товара",)


@fit.callback_query_handler(text="button24")
async def button22(sms: ai.types.message):
    await bot.send_message(sms.from_user.id, f"Выберите какой товар добавить", reply_markup=klav1_5)


@fit.callback_query_handler(text="button25")
async def button22(sms: ai.types.message):
    coll_centr[f"{sms.from_user.id}"][2] = 1
    await bot.send_message(sms.from_user.id, f"Напишите имя товара")


@fit.callback_query_handler(text="button27")
async def button22(sms: ai.types.message):
    coll_centr[f"{sms.from_user.id}"][2] = 3
    await bot.send_message(sms.from_user.id, f"Напишите время доставки товара")


@fit.callback_query_handler(text="button28")
async def button22(sms: ai.types.message):
    coll_centr[f"{sms.from_user.id}"][2] = 4
    await bot.send_message(sms.from_user.id, f"Напишите колличество")


@fit.callback_query_handler(text="button29")
async def button22(sms: ai.types.message):
    db = db_connect("main.db")
    a = coll_centr[f"{sms.from_user.id}"][1]
    db.add_tovars(a[0], coll_centr[f"{sms.from_user.id}"][0][0], a[2], a[3])

    b = db.select('delivery', 'id_user', coll_centr[f"{sms.from_user.id}"][0][0])
    print(b)

    c = db.select('user', 'id', coll_centr[f"{sms.from_user.id}"][0][0])
    print(c)
    db.del_line('coll_delivery', 'id_user', coll_centr[f"{sms.from_user.id}"][0][0])

    await bot.send_message(sms.from_user.id, f"Отправлено")
    await bot.send_message(sms.from_user.id,
                           f'Имя: {c[0][1]} \nТелефон: {c[0][2]} \nАдрес: {c[0][3]} \n \n {tov(b, db)}',
                           reply_markup=klav1_4)


@fit.callback_query_handler(text="button30")
async def button22(sms: ai.types.message):
    coll_centr[f"{sms.from_user.id}"][2] = 5
    await bot.send_message(sms.from_user.id, f"Отправте id товара который необходимо удалить")


# __________________________________________________START_PROGRAM_______________________________________________________


def tov(b1, db1):
    q = ''
    itog = 0
    for i in b1:
        w = db1.select('tovar', 'id', i[0])
        print(w)
        t = f'Название позиции: {w[0][1]} \nЦена: {w[0][2]}\n кол: {i[3]}\n id: {w[0][0]}\n'
        print(t)
        itog += i[3] * w[0][2]
        q = q + t

    itog = f' \nИтог: {itog} \n'
    q = q + itog

    return q


if __name__ == '__main__':
    ai.executor.start_polling(fit, skip_updates=True)

