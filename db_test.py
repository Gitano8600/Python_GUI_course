import sqlite3

con = sqlite3.connect('test.db')
c_obj = con.cursor()

c_obj.execute("CREATE TABLE IF NOT EXISTS balances(id INTEGER PRIMARY KEY, asset TEXT, balance REAL, exchange TEXT)")
con.commit()


def insert_balance(id: int, symbol: str, balance: float, exchange: str):
    c_obj.execute("INSERT INTO balances VALUES(?, ?, ?, ?)", (id, symbol, balance, exchange))
    con.commit()


def update_balance(id: int, balance: float):
    c_obj.execute("UPDATE balances SET balance=? WHERE id=?", (balance, id))
    con.commit()

def sql_fetch_all():
    c_obj.execute("SELECT * from balances")
    result = c_obj.fetchall()
    print(result)


def delete_balance(id: int):
    c_obj.execute("DELETE FROM balances WHERE id=?", (id, ))
    con.commit()


# insert_balance(22, "AVAX", 2, "Bitfinex")

# update_balance(22, 4)

# delete_balance(22)

sql_fetch_all()

c_obj.close()
con.close()