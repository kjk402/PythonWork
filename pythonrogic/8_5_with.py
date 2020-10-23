# # with
# import pickle
#
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))


with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("2020년 9월 11일")
    study_file.write("\npython 개념")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.readline())
