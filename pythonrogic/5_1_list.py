# 리스트[]

subway = [10, 20, 30]

print(subway[1])

subway = ["유재석", "조세호", "박명수"]
print(subway)

#조세호 몇번째?
print(subway.index("조세호"))

# 리스트 추가 append
subway.append("하하")
print(subway)

# 리스트 중간 추가 insert
subway.insert(1, "정형돈")
print(subway)

# 리스트 추출
print(subway.pop())
print(subway)

# count
print(subway.count("유재석"))

# 정렬
num_list = [5,2,4,6,1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

#합치기
num_list.extend(subway)
print(num_list)