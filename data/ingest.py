import pandas as pd
import sqlite3

data = pd.read_csv("data/operations_data.csv")

connection = sqlite3.connect("data/sentinelops.db")

for _, row in data.head(10).iterrows():
    connection.execute("""
        INSERT INTO operations (
            cpu_usage,
            memory_usage,
            response_time,
            error_rate,
            request_rate,
            prediction,
            risk,
            explanation
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        row["cpu_usage"],
        row["memory_usage"],
        row["response_time"],
        row["error_rate"],
        row["request_rate"],
        int(row["label"]),
        "High" if row["label"] == 1 else "Normal",
        "Imported from operations dataset."
    ))

connection.commit()
connection.close()

print("Operations data ingested successfully!")
