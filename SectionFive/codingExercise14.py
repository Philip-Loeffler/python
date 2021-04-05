# take input from user
user_input = input("please enter three numbers: ")

# split the given input into 3 parts
string_tokens = user_input.split(",")

# convert into ints
int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))

# calculate result
a, b, c = int_tokens
results = a + b - c

# result = int_token[0] + int_token[1] - int_token[2]
print(results)
