#문자열
from random import *
sentence = '나는 바보입니다.'
print(sentence)

sentence3 = """
이렇게 출력하면 
줄바꿈도 출력가능
"""
print(sentence3)

python = "Python is Amazing"
print(python)
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python.replace("is", "are"))
print(python)

index1 = python.index("i")
print(index1)
index2 = python.index("i", index1 + 1)
print(index1, index2)

print(python.find("i"))
print(python.count("i"))