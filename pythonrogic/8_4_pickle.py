# 프로그램 상 데이터를 파일로 저장하기

import pickle
profile_file = open("profile.pickle", "wb")
info = {"이름":"박명수", "나이":30, "취미": ["축구", "골프", "영화"]}
print(info)
pickle.dump(info, profile_file) # info에 있는 데이터를 profile_file에 저장한다.
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile_file = pickle.load(profile_file)
print(info)
profile_file.close()