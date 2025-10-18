sentence = "dog is a simple animal dogs is selfless animal"
words=sentence.lower().split()
sets=set(words)
unique_words=len(sets)
print(f"no of unique words:{unique_words}")
