import pandas as pd
import numpy as np

np.random.seed(42)

rows = 1000

cpu_usage = np.random.randint(20, 100, rows)
memory_usage = np.random.randint(30, 100, rows)
response_time = np.random.randint(80, 600, rows)
error_rate = np.round(np.random.uniform(0.0, 0.25, rows), 3)
request_rate = np.random.randint(100, 700, rows)

label = (
    (cpu_usage > 75) |
    (memory_usage > 80) |
    (response_time > 350) |
    (error_rate > 0.10)
).astype(int)

data = pd.DataFrame({
    "cpu_usage": cpu_usage,
    "memory_usage": memory_usage,
    "response_time": response_time,
    "error_rate": error_rate,
    "request_rate": request_rate,
    "label": label
})

data.to_csv("data/operations_data.csv", index=False)

print("1000 realistic records created successfully!")
print(data.head())
print(f"Total records: {len(data)}")
