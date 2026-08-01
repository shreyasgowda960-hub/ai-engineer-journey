with open("week1/day6/test_file3.txt","r")as f:
    w=f.read()
    print(w.split())
    
    y=w.split()
    d={}
    for x in y:
        if x in d:
            d[x]+=1
        else:
            d[x]=1
print(d)            

