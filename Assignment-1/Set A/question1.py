#1. Write a Python program to solve the Tower of Hanoi problem for N disks using Depth-First 
#Search (DFS). Print the sequence of moves and the total number of moves

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    print("Move disk", n, "from", source, "to", destination)

    tower_of_hanoi(n - 1, auxiliary, source, destination)


n = int(input("Enter the number of disks: "))

tower_of_hanoi(n, 'A', 'B', 'C')

print("Total number of moves:", 2**n - 1)
