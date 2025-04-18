# Reverse only the words in a sentence, not the whole string.

str="Hello world"
split_sen=str.split(" ")
rev_word=[]

for word in split_sen:
    rev_word.append(word[::-1])

print(rev_word)
result=" ".join(rev_word)
print(f"Result is {result}")