#Implement a program in Python to represent knowledge using a Semantic Network (Nodes for 
#objects, Edges for relations like is-a, has-a). Write a function to perform simple Inheritance 
#Query (e.g., "Does a dog have four legs?").


# Semantic network represented as a dictionary
semantic_network = {
    "Animal": {
        "is-a": [],
        "has-a": ["four legs"]
    },
    "Dog": {
        "is-a": ["Animal"],
        "has-a": []
    },
    "Cat": {
        "is-a": ["Animal"],
        "has-a": []
    },
    "Bird": {
        "is-a": ["Animal"],
        "has-a": ["two wings"]
    }
}


# Function to check inherited properties
def inheritance_query(node, property_name):
    if node not in semantic_network:
        return False

    # Check the node's own properties
    if property_name in semantic_network[node]["has-a"]:
        return True

    # Check properties inherited from parent nodes
    for parent in semantic_network[node]["is-a"]:
        if inheritance_query(parent, property_name):
            return True

    return False


# Display the semantic network
print("Semantic Network:")
for node, relations in semantic_network.items():
    print(node, ":", relations)

# Test inheritance queries
print("\nInheritance Queries:")

if inheritance_query("Dog", "four legs"):
    print("Does a dog have four legs? Yes")
else:
    print("Does a dog have four legs? No")

if inheritance_query("Cat", "four legs"):
    print("Does a cat have four legs? Yes")
else:
    print("Does a cat have four legs? No")

if inheritance_query("Bird", "two wings"):
    print("Does a bird have two wings? Yes")
else:
    print("Does a bird have two wings? No")

if inheritance_query("Dog", "two wings"):
    print("Does a dog have two wings? Yes")
else:
    print("Does a dog have two wings? No")
