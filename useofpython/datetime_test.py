
# datetime模块的使用
import datetime

# 获取当前日期和时间
now = datetime.datetime.now()
print("当前日期和时间:", now)
# 获取当前日期
today = datetime.date.today()
print("当前日期:", today)
# 获取当前时间
current_time = datetime.datetime.now().time()
print("当前时间:", current_time)

# 创建一个特定的日期
specific_date = datetime.date(2022, 1, 1)
print("特定日期:", specific_date)
# 创建一个特定的日期和时间
specific_datetime = datetime.datetime(2022, 1, 1, 12, 0, 0)
print("特定日期和时间:", specific_datetime)

# 日期和时间的格式化
formatted_date = now.strftime("%Y-%m-%d")
print("格式化后的日期:", formatted_date)
formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
print("格式化后的日期和时间:", formatted_datetime)
# 日期和时间的解析
parsed_date = datetime.datetime.strptime("2022-01-01", "%Y-%m-%d")
print("解析后的日期:", parsed_date)

# 日期和时间的运算
# 计算两日期之间的差异
date1 = datetime.date(2022, 1, 1)
date2 = datetime.date(2022, 1, 10)
date_difference = date2 - date1
print("日期差异:", date_difference.days, "天")
# 一周后的日期
delta = datetime.timedelta(days=7)
print("当前日期:", today)
print("时间间隔:", delta)
next_week = now + delta 
print("一周后的时间:", next_week)
# 获取日期的各个部分
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
print(f"年: {year}, 月: {month}, 日: {day}, 时: {hour}, 分: {minute}, 秒: {second}")
