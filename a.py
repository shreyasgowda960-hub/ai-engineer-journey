words = {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1, 'ran': 1}

for x in words:
    print(words[x])

a={}
a["ck"]=3
a["gk"]=4

print(a)
n = [1, 1, 2, 3, 4,5,6,7,7,6,6]

uc=[]
count=[]

for i in n:
    if i not in uc:
        uc.append(i)
        count.append(1)
    else:
        x=uc.index(i)
        count[x]=count[x]+1
            

print(uc)
print(count)


sentence = "the cat sat on the mat the cat ran"

words=sentence.split()
print(words)

word_count={}

for x in words:
    if x in word_count:
        word_count[x]=word_count[x]+1
    else:
        word_count[x]=1  

print(word_count)