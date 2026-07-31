#A approach

try:
    with open("week1/day6/test_file3.txt","r")as f:
        a=f.readlines()
    print("a:",a)
    print("no. of lines:",len(a))
    total=0
    for x in a:
        words = x.split()
        total = total + len(words)
        # print(len(words))
        # print(words)
    print("no. of words:", total)

except FileNotFoundError:
    print("Missing file")

print("-------------------------Approach B---------------------------------------")


with open("week1/day6/test_file3.txt", "r")as f:
    # a=f.read()
    # # print(a)
    # # for a in f:
    # #     print(a)
    # for x in a:
    #     y=a.split()
    # print(len(y))
    line_count = 0
    total = 0
    for w in f:
        line_count = line_count + 1
        words = w.split()
        total = total + len(words)
print("lines:", line_count)
print("words:", total)

        