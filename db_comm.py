import sqlite3

conn = sqlite3.connect('app_manager.sqlite')
c = conn.cursor()


def check_table(username):

    if username == 'no':
        res = c.execute("SELECT * FROM user")
        return res
    else:
        res = c.execute("SELECT * FROM user where user_name = (?)", (username,))
        return res



def create_user_table():

    c.execute("CREATE TABLE IF NOT EXISTS user (user_name VARCHAR , email VARCHAR )")
    c.close()


def create_job_table():

    c.execute("CREATE TABLE IF NOT EXISTS job (position VARCHAR , date_applied VARCHAR, company VARCHAR, resume VARCHAR, cover_letter VARCHAR, notes VARCHAR, applicant VARCHAR)")
    c.close()


def register(name, email):

    c = conn.cursor()
    c.execute("INSERT INTO user (user_name, email) VALUES (?, ?)", (name, email,),)
    conn.commit()


def add_job(pos, da, comp, resume, cover, notes, app):

    c = conn.cursor()
    c.execute("INSERT INTO job (position, date_applied, company, resume, cover_letter, notes, applicant) VALUES (?, ?, ?, ?, ?, ?, ?)", (pos, da, comp, resume, cover, notes, app,),)
    conn.commit()


def del_entry(id):

    c = conn.cursor()
    c.execute("DELETE FROM job WHERE id=(?)", (id,))
    conn.commit()


def retrieve_jobs(name):

    c = conn.cursor()
    c.execute("SELECT * FROM job where applicant=(?)", (name,))
    x = []
    for y in c.fetchall():
        x.append(y)
    return x

def retrieve_job(id):

    c = conn.cursor()
    c.execute("SELECT * FROM job where id=(?)", (id,))
    return c.fetchone()

    # x = []
    # for y in c.fetchall():
    #     x.append(y)
    # return x
