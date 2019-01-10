string='BANANA'
li=[]
dic={}
for i in range(len(string)):
    for j in range(i+1,len(string)+1):
        li.append(string[i:j])
for i in li:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for k,v in dic.items():
    print(k.center(len(string))," ",v)
