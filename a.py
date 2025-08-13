phrase = "This is a sample phrase."
word = "sample"

index = phrase.index(word)
print(f"The word '{word}' is found at index: {index} and {index + len(word)}")

p2 = "este é um exemplo , exemplificado"
if ' , ' in p2:
    p2 = p2.replace(' , ', ', ')
print(p2)

