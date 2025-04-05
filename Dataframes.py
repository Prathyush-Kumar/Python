import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000]
}

df = pd.DataFrame(data)

print(df, end="\n\n")
print(df.head(2), end="\n\n")
print(df.tail(2), end="\n\n")
print(df.describe(), end="\n\n")
print(df.mean(numeric_only=True), end="\n\n")
print(df['Age'], end="\n\n")
print(df.min(numeric_only=True), end="\n\n")
print(df.max(numeric_only=True), end="\n\n")
print(df.iloc[0, 0], end="\n\n")
