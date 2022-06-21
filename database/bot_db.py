import sqlite3
from config import bot


def sql_create():
    global connection, cursor
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    if connection:
        print('Data connected successfully')
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users
    (telegram_account_id TEXT PRIMARY KEY, 
    username TEXT, 
    user_first_name TEXT, 
    user_last_name TEXT, 
    photo_profile TEXT )
    '''
    connection.execute(
        create_table_query
    )
    connection.commit()


async def sql_insert(state):
    async with state.proxy() as data:
        cursor.execute("""
        INSERT INTO users VALUES (?, ?, ?, ?, ?)
        """, tuple(data.values()))
        connection.commit()


async def sql_select(message):
    for result in cursor.execute('''SELECT * FROM users''').fetchall():
        await bot.send_photo(message.chat.id,
                             result[4],
                             caption=f'Account id: {result[0]}\n'
                                     f'User name: {result[1]}\n'
                                     f'First name: {result[2]}\n'
                                     f'Last name: {result[3]}')


async def sql_select_for_delete():
    return cursor.execute('''SELECT * FROM users''').fetchall()


async def sql_delete(data):
    cursor.execute('''
    DELETE FROM users WHERE telegram_account_id == ?
    ''', (data,))
    connection.commit()
