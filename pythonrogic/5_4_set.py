# 집합 중복안됨, 순서없음

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "박명수"}
python = set(["유재석","조세호"])

#교집합
print(java&python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합
print(java-python)
print(python.difference(java))