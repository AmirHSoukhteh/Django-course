
def count_everything(string):
    l = [c for c in string]
    char_count = 0
    digit_count = 0

    for i in range(l.count(" ")):
        l.remove(" ")

    for c in l:
        if c.isdigit():
            digit_count += 1
        elif c.isalpha():
            char_count += 1
    
    return {"charcaters":char_count, "numbers":digit_count}

result = count_everything(input("enter your text: "))
print(result)
    