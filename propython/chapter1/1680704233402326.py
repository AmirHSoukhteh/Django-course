#[0=wins, 1=loses, 2=draws, 3=goal_difference, 4=point]
table = {"Iran":[0,0,0,0,0], "Spain":[0,0,0,0,0],
         "Portugal":[0,0,0,0,0], "Morocco":[0,0,0,0,0]}
keys = list(table.keys())

for i in range(4):
    for j in range(i+1,4):
        score = [int(i) for i in input().split("-")]
        if score[0]>score[1]:
            table[keys[i]][0] += 1
            table[keys[j]][1] += 1
            table[keys[i]][3] += (score[0]-score[1])
            table[keys[j]][3] += (score[1]-score[0])
            table[keys[i]][4] += 3
            
        elif score[0]==score[1]:
            table[keys[i]][2] += 1
            table[keys[j]][2] += 1
            table[keys[i]][4] += 1
            table[keys[j]][4] += 1
        else:
            table[keys[j]][0] += 1
            table[keys[i]][1] += 1
            table[keys[i]][3] += (score[0]-score[1])
            table[keys[j]][3] += (score[1]-score[0])
            table[keys[j]][4] += 3
            
        score = []

t =  dict(sorted(table.items(), key = lambda x: (-x[1][4],-x[1][0],x[0])))

keys = list(t.keys())

for i in range(4):
    print("%s  wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i"
    %(keys[i], t[keys[i]][0], t[keys[i]][1], t[keys[i]][2], t[keys[i]][3], t[keys[i]][4]))
