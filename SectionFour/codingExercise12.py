number = 5
multiplier = 8
answer = 0

for i in range(multiplier):
    answer += number

print(answer)


# class challenge 1
firstValue = int(input('input a value'))
secondValue = int(input("input another value"))


if firstValue > secondValue:
    print(firstValue)
else:
    print("that value is less")


# class challenge 2
grade = ""
score = int(input("please enter score"))
if score >= 80:
    grade = "A"
elif score >= 60 and score < 80:
    grade = "B"
elif score >= 50 and score < 60:
    grade = "C"
elif score >= 45 and score < 50:
    grade = "D"
elif score >= 25 and score < 45:
    grade = "E"
else:
    grade = "F"

print(grade)
