import datetime

# 생일 입력 받기
birthd = input("생일을 입력하세요 (YYYY-MM-DD): ")
birth = datetime.datetime.strptime(birthd, "%Y-%m-%d").date()

# 현재 년도와 생일의 월, 일로 다음 생일의 날짜 계산
now = datetime.datetime.now().date()
n_birthday = birth.replace(year=now.year)
if n_birthday < now:
    n_birthday = n_birthday.replace(year=now.year + 1)

# 날짜 차이 계산
d_left = (n_birthday - now).days

# 출력
print(f"다음 해 생일까지 {d_left}일 남았습니다.")








# import time

# start_time = input("작업을 시작한 시간을 입력하세요(형식: hh:mm:ss): ")
# end_time = input("작업을 끝낸 시간을 입력하세요(형식: hh:mm:ss): ")

# start_sec = time.mktime(time.strptime(start_time, "%H:%M:%S"))
# end_sec = time.mktime(time.strptime(end_time, "%H:%M:%S"))

# duration_sec = end_sec - start_sec
# duration_min = round(duration_sec / 60)

# print("작업에 걸린 시간은 총", duration_min, "분 입니다.")