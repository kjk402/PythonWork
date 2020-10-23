
url = "http://naver.com"

# http:// 를 빈칸으로 바꿈
my_str = url.replace("http://", "")

print(my_str)

#처음부터 . 전까지 삭제
my_str = my_str[ :my_str.index(".")]

print(my_str)

passwd = my_str[0:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print(passwd)