import pandas as pd
import matplotlib.pyplot as plt

# โหลดข้อมูล
url = "https://raw.githubusercontent.com/asjonats/Baankidteng/0219e55fcd4a1151ddc1427b35abaa31248d3f17/Bann%20Kidteng%20reservation%20-%20reservations%20on%20now.csv"
data = pd.read_csv(url)

# แปลงคอลัมน์ 'date' เป็นชนิดข้อมูล datetime
data['date'] = pd.to_datetime(data['date'])

# สร้างตารางเป็น index โดยใช้คอลัมน์ 'date'
data.set_index('date', inplace=True)

# หาจำนวนการจองในแต่ละเดือน
monthly_bookings = data.resample('M').size()

# พล็อตกราฟแสดงแนวโน้มของจำนวนการจองตามเดือน
plt.figure(figsize=(10, 6))
plt.plot(monthly_bookings)
plt.title('Monthly Bookings')
plt.xlabel('Month')
plt.ylabel('Number of Bookings')
plt.grid(True)
plt.show()
