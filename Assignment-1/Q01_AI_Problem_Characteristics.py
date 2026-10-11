"""
Assignment 1 — Set A — Question 1
Tower of Hanoi using recursive Depth-First Search (DFS).

Run:
    python Q01_Tower_of_Hanoi_DFS.py

The program prints every disk move and the total number of moves.
For N disks, the minimum number of moves is 2**N - 1.
"""

def tower_of_hanoi(n, source, auxiliary, destination, move_count):
    """Move n disks from source to destination using auxiliary."""
    if n == 1:
        move_count[0] += 1
        print(f"Move {move_count[0]}: Move disk 1 from {source} to {destination}")
        return

    # First explore the subproblem of moving n-1 disks out of the way.
    tower_of_hanoi(n - 1, source, destination, auxiliary, move_count)

    # Move the largest disk to the destination peg.
    move_count[0] += 1
    print(f"Move {move_count[0]}: Move disk {n} from {source} to {destination}")

    # Then move the n-1 disks onto the largest disk.
    tower_of_hanoi(n - 1, auxiliary, source, destination, move_count)


def main():
    try:
        n = int(input("Enter the number of disks: "))
        if n < 1:
            print("Please enter a positive integer (at least 1).")
            return
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    move_count = [0]
    print("\nSequence of moves:")
    tower_of_hanoi(n, "A", "B", "C", move_count)
    print(f"\nTotal number of moves: {move_count[0]}")


if __name__ == "__main__":
    main()
