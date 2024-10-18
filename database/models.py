import sqlite3

def init_db():
    connection = sqlite3.connect('rules.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS rules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rule_string TEXT NOT NULL,
        ast TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    connection.commit()
    connection.close()

def save_rule(rule_string, ast):
    connection = sqlite3.connect('rules.db')
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO rules (rule_string, ast)
                      VALUES (?, ?)''', (rule_string, ast))

    connection.commit()
    connection.close()
