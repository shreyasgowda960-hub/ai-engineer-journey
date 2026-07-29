#splitting words

sentence = "the cat sat on the mat the cat ran"

words=sentence.split()

print(words)

#conversion 

a="Cat"

b="mr george"
print(a.lower())
print(a.upper())
print(b.title())

#cleaning

messy="  hello world!!!    "

print(messy.strip())
messy1=messy.strip()
print(messy1.replace("!",""))

#searching and counting

text="mississippi"

print(text.count("ss"))

print("ss" in text)

print(text.find("pp"))

sentence = "the cat sat on the mat the cat ran"

print(sentence.split())
words=sentence.split()
print(words)
count_of_words=words.count("cat")
print(count_of_words)

words_count={}

for word in words:
    if word in words_count:
        words_count[word] = words_count[word] + 1
    else:
        words_count[word] = 1

print(words_count)