num = int(input())
dic = {}

for i in range(num):
    word = input().split(" ")
    name = word.pop(0)
    dic[name] = word

letter = input().split()
key = dic.keys()

for i in letter:
    for k in key:
        if i in dic[k]:
            letter = list(map(lambda x: x.replace(i, k), letter))
            
print(" ".join(letter))
