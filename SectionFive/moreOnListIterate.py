available_parts = ["computer", "monitor",
                   "keyboard", "mouse", "mouse mat", "hdmi cable", "dvd drive"]
current_choice = "-"
computer_parts = []
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
while current_choice != '0':
    if current_choice in valid_choices:
        print("adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_parts = available_parts[index]
        computer_parts.append(chosen_parts)

    else:
        print("please add options fomr the list below")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print(computer_parts)


# comprehension
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
