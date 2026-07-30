#comprehension sq of even no from 0-20

even_squares=[x*x for x in range(0,21) if x%2==0]
print(even_squares)

even_squares_dict={x:x*x for x in range(0,21) if x%2==0}

print(even_squares_dict)

#Palindrome Checker

def is_palindrome(word):
    word=word.lower()
    if word==word[::-1]:
        return True
    else:
        return False

print(is_palindrome("nana"))

print(is_palindrome("nan"))


