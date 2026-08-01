print("Welcome to TODOLIST\nTo edit file:a\nTo read file:r\nTo quit:q")
# a=""
# r=""
# q=""
x=input("Enter choice\na\nr\nq\n")

while True:
    x=input("Enter choice\na\nr\nq\n")

    try:
            
        if x=="a":
            with open("week1/day7/todol.txt","a")as f:
                    f.write(input("Enter Your ToDoList: ")+(f"\n"))
                    print("ToDoList updated")
            break
        elif x=="r":
                with open("week1/day7/todol.txt","r")as f:
                        lines=f.read()
                        print(lines)
                        break
                        
        elif x=="q":
            print("Quitting...........................")                
            break
        else:
              print("invalid choice ")
    except FileNotFoundError:
          print("no file ")
          continue    
                    
                 
             