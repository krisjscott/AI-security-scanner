import sqlite3

def get_user_data(username):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    rows = c.fetchall()
    conn.close()
    return rows

malicious_username = "admin' OR '1'='1'"
print(get_user_data(malicious_username))