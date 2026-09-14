import sqlite3

connection = sqlite3.connect("data/sentinelops.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS operations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpu_usage REAL,
    memory_usage REAL,
    response_time REAL,
    error_rate REAL,
    request_rate REAL,
    prediction INTEGER,
    risk TEXT,
    explanation TEXT
)
""")

connection.commit()
connection.close()

print("Operations table created successfully!")
