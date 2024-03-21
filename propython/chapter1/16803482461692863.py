# stupid olympiad

num = int(input())

#all_id = all student information
#f_id = Female, m_id = Male
all_id=[]
f_id=[]
m_id=[]

def information():
    '''
    give information and made id list
    then made list of information every student ...
    
    '''
    id = str(input()).split(".")
    id[1] = id[1].title()
    all_id.append(id)
    for sub in all_id:
        if sub[0]=='f':
            f_id.append(sub)
            all_id.pop(all_id.index(sub))
        if sub[0]=='m':
            m_id.append(sub)
            all_id.pop(all_id.index(sub))
    
def sort(sub_li):
    '''sort by Alphabet'''
    sub_li.sort(key = lambda x: x[1])
    return sub_li

for i in range(num):
    information()

f_id = sort(f_id)
m_id = sort(m_id)

x = len(f_id)
y = len(m_id)
for i in range(x):
    print(' '.join(f_id[i]))
for i in range(y):
    print(' '.join(m_id[i]))
