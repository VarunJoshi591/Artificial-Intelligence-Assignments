"""
Assignment 1 — Question 1
List four common characteristics of a problem solved by AI.

This beginner-friendly script displays the four characteristics recorded
in the assignment notes, along with a brief explanation of each one.
It is a study aid, not an AI algorithm.
"""

characteristics = {
    "1. Complexity and ambiguity":
        "The problem may have many possible solutions or incomplete information.",
    "2. Need for learning or adaptation":
        "The system may need to learn from experience or adapt to new data.",
    "3. Large or unstructured data":
        "The problem may involve text, images, audio, or other complex data.",
    "4. Human-like decision-making or perception":
        "The system may need to recognize patterns, interpret inputs, or choose actions.",
}

print("Four Common Characteristics of AI Problems\n")

for characteristic, explanation in characteristics.items():
    print(characteristic)
    print(f"   {explanation}\n")
