word=input("Enter to check Palindrome: ")


while word.isdigit():
    print("you've entered a num try again")
    word=input("Enter to check Palindrome: ")


if word==word[::-1]:
    print(f"The word:'{word}' you entered is a Palindrome")
else:
    print(f"The word:'{word}' you entered is not a Palindrome")    

    