text = input()
sentence = text.split(". ")
index_words = []
count = 1
for j in range(len(sentence)):
    words = sentence[j].split(" ")
    for i in range(len(words)):
        if words[i][0].isupper() and i>0:
            index_words.append((words[i], count))
        if not words[i][-1].isalpha():
            words[i] = words[i][:-1]
        if words[i].isdigit():
            count += 1
        elif words[i][-1] == ',' or words[i][-1] == '.':
            words[i] = words[i][:-1]
            count += 1
        else:
            count += 1

if len(index_words) == 0:
    print("None")
else:
    for word in index_words:
        print(word[1],":", word[0].replace(".","").replace(",",""),sep ="")

