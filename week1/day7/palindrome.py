word=input("Enter to check Palindrome: ")


if word.isdigit():
    print("you've entered a num try again")
elif word==word[::-1]:
    print(f"The word:'{word}' you entered is a Palindrome")
else:
    print(f"The word:'{word}' you entered is not a Palindrome")    

    