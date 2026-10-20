#Implement the Naïve Bayes classifier model to predict a class (e.g., 'play tennis' or 'not play 
#tennis') from a given dataset (e.g., weather data). Calculate the prior probability and likelihood 
#for each feature.

# Resolution Refutation Example
# Knowledge:
# 1. All humans are mortal.
# 2. Socrates is human.
# Goal: Socrates is mortal.

# Convert to clauses:
#
# All humans are mortal:
# NOT(Human(x)) OR Mortal(x)
#
# Socrates is human:
# Human(Socrates)
#
# Negation of goal:
# NOT(Mortal(Socrates))


clauses = [
    {"NOT Human(x)", "Mortal(x)"},
    {"Human(Socrates)"},
    {"NOT Mortal(Socrates)"}
]

print("Initial Clauses:")
for clause in clauses:
    print(clause)


# Resolution

print("\nResolution Steps:")

print("1. Human(Socrates)")
print("2. NOT Human(x) OR Mortal(x)")
print("--------------------------------")
print("3. Mortal(Socrates)")

print("\nNow:")
print("Mortal(Socrates)")
print("NOT Mortal(Socrates)")
print("--------------------------------")
print("Empty Clause: {}")

print("\nConclusion:")
print("The statement 'Socrates is mortal' is TRUE.")