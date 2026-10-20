#Implement a program to demonstrate the Resolution Refutation Principle in First-Order Logic. 
#Convert a set of given sentences into Conjunctive Normal Form (CNF) and use resolution to 
#prove or disprove a statement.


def resolve(clause1, clause2):
    result = []

    for literal1 in clause1:
        for literal2 in clause2:

            # Check for complementary literals
            if literal1 == "~" + literal2 or literal2 == "~" + literal1:

                new_clause = []

                for literal in clause1:
                    if literal != literal1:
                        new_clause.append(literal)

                for literal in clause2:
                    if literal != literal2 and literal not in new_clause:
                        new_clause.append(literal)

                result.append(new_clause)

    return result


def resolution(kb, query):
    clauses = kb.copy()

    # Negate the query and add it to the knowledge base
    clauses.append(["~" + query])

    print("Initial CNF Clauses:")
    for clause in clauses:
        print(clause)

    print("\nResolution Steps:")

    while True:
        new_clauses = []

        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):

                resolvents = resolve(clauses[i], clauses[j])

                for resolvent in resolvents:

                    # Empty clause indicates contradiction
                    if not resolvent:
                        print(clauses[i], "+", clauses[j], "=> []")
                        print("\nContradiction found!")
                        print("Statement is PROVED.")
                        return

                    if resolvent not in clauses and resolvent not in new_clauses:
                        new_clauses.append(resolvent)
                        print(clauses[i], "+", clauses[j], "=>", resolvent)

        if not new_clauses:
            print("No contradiction found.")
            print("Statement could not be proved.")
            return

        clauses.extend(new_clauses)


# Knowledge Base converted into CNF
# All humans are mortal: ~Human(x) OR Mortal(x)
# Socrates is a human: Human(Socrates)

kb = [
    ["~Human(Socrates)", "Mortal(Socrates)"],
    ["Human(Socrates)"]
]

# Statement to prove
query = "Mortal(Socrates)"

resolution(kb, query)
