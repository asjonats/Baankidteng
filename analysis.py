import pandas as pd

# โหลดข้อมูล CSV
url = "https://github.com/asjonats/Baankidteng/raw/68c0f1b862644220c5ee4f8db32141d90948bf7e/Bann%20Kidteng%20reservation%20-%20reservations%20on%20now.csv"
df = pd.read_csv(url)


print(df['dateIn'].dtypes)

# แปลงคอลัมน์ 'reserve_date' เป็นรูปแบบวันที่
df['date'] = pd.to_datetime(df['dateIn'])

print(df.head())
print(df.dtypes)


