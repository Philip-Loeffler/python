age = int(input("how old arer you "))

if age >= 16 and age <= 65:
    print("have a god day at work")

# using or, the analogy falls down slight in english because there is an implication that you can only
# have one or the other
# in programming languages, both conditions COULD BE true


# simplified chained comparisons
# this is the same as the other one
if 16 <= age <= 65:
    print("have a good day at work")
else:
    print("enjoy your free time")
print("-" * 80)

if age < 16 or age > 65:  # will get if either condition is true
    print("enjoy your free time")
else:
    print("have a good day at work")

# when comparing conditons using and, python will stop checking as soon as it finds a conditon that is false
# when comparing conditions using or, it will satop as soon as it finds one that is true
