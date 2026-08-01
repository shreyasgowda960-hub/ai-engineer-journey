with open("week1/day6/test_file3.txt","r")as f:
    w=f.readlines()
    print(w)
    print(len(w))
    t=0
    for x in w:
        n=x.split()
        # print(len(n))

        
        print(f"Each line length",len(n))
        t+=len(n)
    
print(t)    
        