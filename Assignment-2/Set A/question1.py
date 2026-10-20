#Write a Prolog program to represent a small family tree. Define facts for parent, male, and 
#female. Write rules for relationships like mother, father, sibling, and grandparent. Test various 
#queries.


parents = [
    ("John", "Alice"),
    ("John", "Bob"),
    ("Mary", "Alice"),
    ("Mary", "Bob"),
    ("Alice", "David")
]

males = ["John", "Bob", "David"]
females = ["Mary", "Alice"]

# Rule: Mother
def mother(x, y):
    return (x, y) in parents and x in females

# Rule: Father
def father(x, y):
    return (x, y) in parents and x in males

# Rule: Sibling
def sibling(x, y):
    for parent in set(p[0] for p in parents):
        children = [child for p, child in parents if p == parent]

        if x in children and y in children and x != y:
            return True

    return False

# Rule: Grandparent
def grandparent(x, y):
    for child in [c for p, c in parents if p == x]:
        if (child, y) in parents:
            return True

    return False


# Test queries

print("Is Mary mother of Alice?", mother("Mary", "Alice"))
print("Is John father of Bob?", father("John", "Bob"))
print("Are Alice and Bob siblings?", sibling("Alice", "Bob"))
print("Is John grandparent of David?", grandparent("John", "David"))
