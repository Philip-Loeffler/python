
sampleText = "python is a very powerful language"
# could also do vowels = {"a", "e", "i", "o", "u"}
vowels = frozenset("aeiou")
finalSet = set(sampleText).difference(vowels)
print(finalSet)

finalList = sorted(finalSet)
print(finalList)
