def is_palindrome(w):
    w=w.lower()
    return w==w[::-1]

u=is_palindrome(input("say"))
print(u)

