import random

doc = { "names" : ["준기","승기","길동", "알고", "메튜"]}
with open("info.txt", "w" ) as file :
    for i in range(5):
        name = random.choice(doc["names"])
        weight = random.randrange(40, 100)
        height = random.randrange(150, 190)

        file.write("{}, {}, {}\n".format(name, weight, height))


# with open("info.txt", "r") as file:
#     contents = file.read()
# print(contents)