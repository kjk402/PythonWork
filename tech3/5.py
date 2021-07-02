def solution(penter, pexit, pescape, data):

    stack = ""

    for j in range(0, len(data), len(penter)):
        if data[j:j+len(penter)] == penter or data[j:j+len(penter)] == pexit or data[j:j+len(penter)] == pescape:
            stack += pescape
            stack += data[j:j+len(penter)]
        else:
            stack += data[j:j+len(penter)]

    return penter +stack+pexit

e = "10"
exit = "11"
scape = "00"
data = "00011011"
# e = "1100"
# exit = "0010"
# scape = "1001"
# data = "1101100100101111001111000000"
print(solution(e, exit, scape, data))

print(data[0:2])
print(data[2:4])
print(data[4:6])