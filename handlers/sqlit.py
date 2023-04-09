import sqlite3

def reg_user(id, refka):
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute(""" CREATE TABLE IF NOT EXISTS black_list (
            id BIGINT,
            stat
            ) """)
    db.commit()

    sql.execute(""" CREATE TABLE IF NOT EXISTS user_time (
        id BIGINT,
        prokladka,
        finish_stat
        ) """)
    db.commit()

    sql.execute(f"SELECT id FROM user_time WHERE id ='{id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user_time VALUES (?,?,?)", (id,refka,'0'))
        db.commit()



def info_members(): # Количество челов, запустивших бота
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    a = sql.execute(f'SELECT COUNT(*) FROM user_time').fetchone()[0] # Всего пользователей
    q = sql.execute(f'SELECT COUNT(*) FROM user_time WHERE finish_stat = "1"').fetchone()[0] # Прошли обучение

    b11 = sql.execute(f'SELECT COUNT(*) FROM user_time WHERE finish_stat = "11"').fetchone()[0]  # Прошли обучение
    b22 = sql.execute(f'SELECT COUNT(*) FROM user_time WHERE finish_stat = "22"').fetchone()[0]  # Прошли обучение
    b33 = sql.execute(f'SELECT COUNT(*) FROM user_time WHERE finish_stat = "33"').fetchone()[0]  # Прошли обучение
    b44 = sql.execute(f'SELECT COUNT(*) FROM user_time WHERE finish_stat = "44"').fetchone()[0]  # Прошли обучение
    b55 = sql.execute(f'SELECT COUNT(*) FROM user_time WHERE finish_stat = "55"').fetchone()[0]  # Прошли обучение
    b66 = sql.execute(f'SELECT COUNT(*) FROM user_time WHERE finish_stat = "66"').fetchone()[0]  # Прошли обучение
    b77 = sql.execute(f'SELECT COUNT(*) FROM user_time WHERE finish_stat = "77"').fetchone()[0]  # Прошли обучение

    return a,b11,b22,b33,b44,b55,b66,b77,q

def change_status(id,num):
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    q = sql.execute(f"SELECT finish_stat FROM user_time WHERE id = '{id}'").fetchone()
    try:
        q = q[0]
    except:
        pass

    if q == None:
        print(" Не обновляем. Это старый", id)
    else:
        print("Обновляем. Это новый", id)
        sql.execute(f"UPDATE user_time SET finish_stat = '{num}' WHERE id = '{id}'")
        db.commit()




def change_prokladka(id, p):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE user_time SET prokladka = '{p}' WHERE id = '{id}'")
    db.commit()

def add_black(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute(f"SELECT id FROM black_list WHERE id = '{id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO black_list VALUES (?,?)", (int(id), '0'))
        sql.execute(f"INSERT INTO black_list VALUES (?,?)", (str(id), '0'))
        db.commit()

def get_username(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    q = (sql.execute(f"SELECT prokladka FROM user_time WHERE id = '{id}'").fetchone())[0]
    return q



def cheak_black(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"SELECT id FROM black_list WHERE id = '{id}'")
    if sql.fetchone() is None: #Список пуст, разрешает
        return 0
    else: #Запрещаем
        return 1