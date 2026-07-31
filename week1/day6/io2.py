#writing
with open("week1/day6/test_file2.txt", "w") as f:
    f.write("This is a test file now erased old data")


#appending
with open("week1/day6/test_file2.txt", "a") as f:
    f.write(". This is the appended data")

#writing 
with open("week1/day6/test_file3.txt", "w") as f:
    f.write("This is line 1\n")
    f.write("This is line 2\n")
    f.write("This is line 3")

#reading op1
with open("week1/day6/test_file3.txt", "r") as f:
    w=f.read()
    print(w)

#reading op2
with open("week1/day6/test_file3.txt", "r") as f:
    content=f.readlines()
    print(content)

#reading op2.1
with open("week1/day6/test_file3.txt", "r") as f:
    content=f.readline()
    c2=f.readline()
    print(content,c2)
    print(content+c2)

#reading op3
with open("week1/day6/test_file3.txt", "r") as f:
    for x in f:
        print(x)



