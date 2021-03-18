
# telling the sorted function the name of another function that sorted should use
# so by doing this we wont have the capital T in the front of the list
missing_letter = sorted(
    "the quick brown fox jumped over the lazy dog",  key=str.casefold)
print(missing_letter)


names = ["Grahm",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"]

names.sort(key=str.casefold)
print(names)
# this will return:
# ['eric', 'Graham', "John", 'michael', 'terry', 'Terry'],
