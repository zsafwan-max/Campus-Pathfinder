# main.py
# Run this file to try the campus pathfinder

from pathFindupdate import Graph, BUILDINGS, dijkstra, format_result

def print_menu():
    print("\n=== Campus Pathfinder ===")
    print("Choose mode:")
    print("  1) Shortest path (minimize walking time)")
    print("  2) Accessible path (prefer accessible routes)")
    print("  3) Exit")

def choose_building(prompt, graph):
    print("\nAvailable buildings:")
    for i, b in enumerate(BUILDINGS, start=1):
        print(f"  {i}. {b}")
    choice = input(f"\n{prompt} (type name or number): ").strip()
    # allow number or exact name
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(BUILDINGS):
            return BUILDINGS[idx]
    # otherwise, try to match name (case-insensitive)
    for b in BUILDINGS:
        if choice.lower() == b.lower():
            return b
    print("Invalid building selection.")
    return None

def main():
    graph = Graph()

    while True:
        print_menu()
        sel = input("Enter choice: ").strip()
        if sel == "3":
            print("Goodbye — have a nice day!")
            break
        if sel not in ("1", "2"):
            print("Please enter 1, 2, or 3.")
            continue

        mode = "distance" if sel == "1" else "accessible"
        start = choose_building("Enter start building", graph)
        if not start:
            continue
        end = choose_building("Enter destination building", graph)
        if not end:
            continue

        print(f"\nCalculating {mode} path from {start} to {end}...\n")
        path, cost, trace = dijkstra(graph, start, end, mode=mode)

        # Step-by-step trace (Option B)
        if trace:
            print("Trace (steps explored to build the found path):")
            for t in trace:
                print("  -", t)
            print()

        print(format_result(path, cost, mode))

if __name__ == "__main__":
    main()
