types_of_people = 10

binary = "binary"
do_not = "don't"

y = f"Those who know {binary} and those who {do_not}"

x = f"There are {types_of_people} types_of_people."

print(x)
print(y)

print(f"I said: '{x}'")
print(f"I also said: '{y}'")

hilarious = "False"
joke_evaluation = "Isn't that joke so funny?!{}"
print(joke_evaluation.format(hilarious))
