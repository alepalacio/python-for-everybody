word = "banana"

count = 0
for letter in word:
    if letter:
        count = count + 1
print(count)
print(word[0:4])
print(word[3:20])
print(word[:])
print(word[3:])
print(word[:4])

if "a" in word:
    print("Found letter A")
    
word1 = "Hello Palacio"
lower_word = word1.lower()
print(lower_word)
print(word1.lower())
print("Hello Palacio".lower())
print(type(word1))
print(dir(word1))