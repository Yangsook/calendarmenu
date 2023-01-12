# from django.test import TestCase
# import calendar
# import pandas as pd
# # from .models import Menu

# df = pd.read_excel('menu.xlsx', 'menu')
# df_list = df.values.tolist()

# print(df, '\n')
# # print(df_list)

# for item in df_list:
#     print(item)
    # db = Menu()
    # db.menu = item[0]
    # db.meal = item[1]
    # db.category = item[2]

    # db.save()





# cal = calendar.calendar()

# calendar.setfirstweekday(calendar.SUNDAY)
# print(calendar.month(2022,12))
# print(calendar._nextmonth(2022,12))
# print(calendar.monthrange(2022,12))  # 시작하는 1일의 요일과 마지막날의 날짜를 리턴
# print(calendar.weekday(2022,12,31))  # 월(0), 화(1) ~ 토(5), 일(6)
# print(calendar.monthcalendar(2022,12))  # 리스트형식으로 리턴 [[0, 0, 0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25], [26, 27, 28, 29, 30, 31, 0]]


# 다음은 Calendar가 가진 클래스 어트리뷰트이다.

# calendar.day_name : 현재 로케일의 요일을 나타내는 배열이다.
# calendar.day_abbr : 현재 로케일의 약식 요일을 나타내는 배열이다.
# calendar.month_name : 현재 로케일의 연중 월을 나타낸다.
# calendar.mont_abbr : 현재 로케일의 연중 월을 약식으로 나타낸다.


# my_cal = calendar.HTMLCalendar(firstweekday=6)
# print(my_cal.formatmonth(2023, 1, withyear=True))




# 년도의 월을 출력하기

# import calendar
# import datetime
# import sys
# tr= str(datetime.date.today()).split("-")  # 2022-12-31
# year = int(tr[0])
# month = int(tr[1])
# l = ["S","M","T","W","T","F","S"]
# day = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

# print("CALENDAR",year,month)
# for x in range(len(l)):
#     print("   ",end = "")
#     print(l[x],end = "")
# print()

# c = list(calendar.monthrange(year,month))   # 시작하는 1일의 요일과 마지막날의 날짜를 리턴
# tc = {0:1,1:2,2:3,3:4,4:5,5:6,6:0}
# c[0] = tc[c[0]]

# cnt = 0
# t = []
# for x in range(7):
#     for g in range(7):
#         if cnt+1 >= 10:
#             print("  ",end = "")
#         else:
#             print("   ",end = "")

#         if x == 0 and g == c[0]:
#             cnt += 1
#         elif not x == 0 or g >= c[0]:
#             cnt += 1

#         if cnt > 0:
#             print(cnt,end = "")
#         else:
#             print(end = " ")
#         t.append(cnt)

#         if cnt >= c[1]:
#             print()
#             sys.exit()
#     print()
