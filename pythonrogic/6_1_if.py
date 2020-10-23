#if
from random import *
weather = ["rain","sunny","dust","snow"]
shuffle(weather)
today = weather.pop()
print(today)

if today == "rain" or today == "snow":
    print("우산을 챙기세요.")
elif today == "sunny":
    print("오늘은 맑음입니다.")
else:
    print("마스크 착용하세요.")

# weather = input("오늘날씨는?")
# if weather == "rain":
#     print("우산을 챙기세요.")
# elif weather == "sunny":
#     print("오늘은 맑음입니다.")
# else:
#     print("마스크 착용하세요.")

# temp = int(input("기온이 어때요?"))
temp = randrange(-10,35)
print(temp)
if temp >=25:
    print("덥습니다.")
elif temp <= 3:
    print("춥습니다")
else:
    print("온화합니다.")