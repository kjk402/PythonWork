# 출석번호 1,2,3,4 에 100을 더하기
#
student = range(1,5)
print(type(student))
student = list(student)
print(type(student))
print(student)

student = [i+100 for i in student]
print(student)


# 학생 이름 길이로 변환

students= ["Iron man", "Thor", "Groot"]
students = [len(i) for i in students]
print("\n"+str(students))

# 대문자로 변환

students= ["Iron man", "Thor", "Groot"]
students= [i.upper() for i in students]
print(students)