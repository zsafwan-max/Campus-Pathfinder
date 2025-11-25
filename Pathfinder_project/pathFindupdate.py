from minHeap import MinHeap

# --- Building List ---
BUILDINGS = [
    "Parking Garage",             # PARK
    "Core Science Facility",      # CSF
    "University Centre",          # UC
    "Earth Science Building",     # ES
    "Engineering Building",       # EN
    "Business Building",          # BUS
    "Chapel",                     # CHAPEL
    "Dorms",                      # DORMS
    "Chemistry/Physics Building", # CP
    "Old Science Building",       # OLD SCI
    "Arts & Administration",      # A&A
    "Bruneau Centre",             # BRUNEAU
    "Library",                    # LIB
    "HKR (Human Kinetics)",       # HKR
    "The Works (Recreation)",     # WORKS
    "Education Building",         # EDUC
]

# --- Graph Class ---
class Graph:
    def __init__(self):
        # Dictionary: { node: [(neighbor, minutes, accessibility, label), ...] }
        self.edges = {}
        self._build_graph()

    def add_edge(self, a, b, minutes, accessibility=8, label="walk"):
        """Add a directed edge between two nodes."""
        if a not in self.edges:
            self.edges[a] = []
        self.edges[a].append((b, minutes, accessibility, label))

    def neighbors(self, node):
        return self.edges.get(node, [])

    def _build_graph(self):
        """Build the full MUN building graph based on realistic walking distances."""
        def both(a, b, minutes, accessibility=8, label="walk"):
            self.add_edge(a, b, minutes, accessibility, label)
            self.add_edge(b, a, minutes, accessibility, label)

        # --- Parking Garage Connections ---
        both("Parking Garage", "Core Science Facility", 3, 9, "walkway")
        both("Parking Garage", "University Centre", 4.5, 8, "path")
        both("Parking Garage", "Engineering Building", 7, 7, "sidewalk")
        both("Parking Garage", "The Works (Recreation)", 6, 7, "outdoor walk")

        # --- Campus Connections (existing from before) ---
        both("Core Science Facility", "University Centre", 4, 9, "tunnel/covered")
        both("University Centre", "Earth Science Building", 4, 9, "covered walkway")
        both("Earth Science Building", "Engineering Building", 3, 9, "short link")
        both("Engineering Building", "Business Building", 3, 6, "outdoor walk")
        both("Business Building", "Chapel", 4, 6, "outdoor walk")
        both("Chapel", "Dorms", 5, 5, "outdoor walk")
        both("Dorms", "Chemistry/Physics Building", 5, 9, "tunnel")
        both("Chemistry/Physics Building", "Old Science Building", 4, 8, "corridor")
        both("Old Science Building", "Arts & Administration", 2, 6, "outdoor walk")
        both("Arts & Administration", "Bruneau Centre", 4, 7, "outdoor walk")

        # Bruneau ↔ Library (two routes)
        self.add_edge("Bruneau Centre", "Library", 3, 9, "tunnel")
        self.add_edge("Library", "Bruneau Centre", 3, 9, "tunnel")
        self.add_edge("Bruneau Centre", "Library", 2, 7, "outdoor walk")
        self.add_edge("Library", "Bruneau Centre", 2, 7, "outdoor walk")

        both("Library", "HKR (Human Kinetics)", 3, 9, "tunnel")
        both("HKR (Human Kinetics)", "The Works (Recreation)", 3, 9, "indoor link")
        both("Library", "The Works (Recreation)", 5, 7, "outdoor walk")

        # Library ↔ Education (two routes)
        self.add_edge("Library", "Education Building", 4.5, 9, "tunnel route")
        self.add_edge("Education Building", "Library", 4.5, 9, "tunnel route")
        self.add_edge("Library", "Education Building", 3.5, 7, "outdoor walk")
        self.add_edge("Education Building", "Library", 3.5, 7, "outdoor walk")

        # Works ↔ Education (two routes)
        self.add_edge("The Works (Recreation)", "Education Building", 3.5, 9, "tunnel link")
        self.add_edge("Education Building", "The Works (Recreation)", 3.5, 9, "tunnel link")
        self.add_edge("The Works (Recreation)", "Education Building", 5.5, 7, "outdoor walk")
        self.add_edge("Education Building", "The Works (Recreation)", 5.5, 7, "outdoor walk")

        # UC ↔ Chemistry/Physics (two routes)
        self.add_edge("University Centre", "Chemistry/Physics Building", 3, 9, "overhead pass")
        self.add_edge("Chemistry/Physics Building", "University Centre", 3, 9, "overhead pass")
        self.add_edge("University Centre", "Chemistry/Physics Building", 4.5, 7, "outdoor route")
        self.add_edge("Chemistry/Physics Building", "University Centre", 4.5, 7, "outdoor route")

        # Ensure all nodes exist
        for b in BUILDINGS:
            if b not in self.edges:
                self.edges[b] = []

# --- Dijkstra Algorithm ---
def dijkstra(graph, start, end, mode="shortest"):
    """
    Dijkstra's algorithm for shortest or most accessible path.
    mode = "shortest" → minimize minutes
    mode = "accessible" → prefer high accessibility (adds small penalties)
    """
    distances = {node: float('inf') for node in graph.edges}
    previous = {node: None for node in graph.edges}
    distances[start] = 0

    heap = MinHeap()
    heap.insert((0, start))

    while not heap.is_empty():
        current_distance, current_node = heap.extract_min()

        if current_distance > distances[current_node]:
            continue

        if current_node == end:
            break

        for neighbor, minutes, access, label in graph.neighbors(current_node):
            if mode == "accessible":
                penalty = (10 - access) * 0.2
                new_distance = current_distance + minutes + penalty
            else:
                new_distance = current_distance + minutes

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = (current_node, label)
                heap.insert((new_distance, neighbor))

    # Reconstruct path
    path = []
    node = end
    while previous[node]:
        prev, label = previous[node]
        path.append((prev, node, label))
        node = prev
    path.reverse()

    return path, distances[end]

# --- Helper: Format result ---
def format_result(path, total_time):
    if not path:
        return "No available path found."

    result = "\nRoute Summary:\n"
    for i, (a, b, label) in enumerate(path, 1):
        result += f"  {i}. {a} → {b}  ({label})\n"

    result += f"\nEstimated total travel time: {round(total_time, 2)} minutes\n"
    return result

# --- Run test ---
if __name__ == "__main__":
    g = Graph()

    print("Memorial University Campus Pathfinder\n")
    print("Available Buildings:")
    for i, b in enumerate(BUILDINGS, 1):
        print(f"{i}. {b}")

    start_idx = int(input("\nEnter start building number: ")) - 1
    end_idx = int(input("Enter destination building number: ")) - 1

    print("\nSelect route mode:")
    print("1. Shortest route")
    print("2. Accessible route")
    mode_choice = input("Enter 1 or 2: ")
    mode = "accessible" if mode_choice == "2" else "shortest"

    start = BUILDINGS[start_idx]
    end = BUILDINGS[end_idx]

    path, total_time = dijkstra(g, start, end, mode)
    print(format_result(path, total_time))
