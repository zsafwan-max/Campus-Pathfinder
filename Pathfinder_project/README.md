 Memorial University Campus Pathfinder (Python)

A Python project that calculates the fastest or most accessible walking routes between buildings at Memorial University of Newfoundland (MUN) using a custom graph, manual MinHeap, and Dijkstra’s Algorithm.

This project demonstrates core data-structures knowledge and algorithm implementation without relying on built-in libraries like heapq.

 Overview

Campus Pathfinder is a terminal-based tool that allows users to:

Select a start and destination building

Choose Shortest Route or Most Accessible Route

Receive a step-by-step path with total estimated time

The program uses real walking times and building connections based on MUN’s campus layout.

 Key Features

✔️ Custom Graph implementation (adjacency list)
✔️ Manual MinHeap built from scratch
✔️ Dijkstra’s Algorithm fully implemented manually
✔️ Two routing modes

Shortest: minimizes minutes

Accessible: avoids outdoor/low-access routes

✔️ Realistic building connections (tunnels, overhead passes, outdoor paths)
✔️ Well-structured and easy to expand

 Buildings Included

Core Science Facility

University Centre

Earth Science Building

Engineering Building

Business Building

Chapel

Dorms

Chemistry/Physics Building

Old Science Building

Arts & Administration

Bruneau Centre

Library

HKR (Human Kinetics)

The Works (Recreation)

Education Building

Parking Garage

 Project Structure
Campus-Pathfinder/
│
├── pathFindUpdate.py       # Graph + Dijkstra + building connections
├── minHeap.py              # Custom MinHeap (insert, extract_min, etc.)
├── main.py                 # CLI runner (user input + output formatting)
├── README.md               # Documentation
└── (optional) assets/      # Campus map images

 How It Works
1. Graph Construction

pathFindUpdate.py builds a graph where each edge includes:

walking time (minutes)

accessibility rating

connection type (tunnel, outdoor, overhead)

2. MinHeap (Manual)

minHeap.py contains:

insert()

extract_min()

heapify_up()

heapify_down()

This shows your understanding of heap operations without using Python’s built-ins.

3. Dijkstra’s Algorithm

Used to compute the:

fastest route, or

most accessible route (penalty added to low-access edges)

4. CLI Interaction

main.py asks the user for:

start building

destination

mode

Then prints the full route.

 How to Run the Program
1. Open Terminal in the Project Folder

On Mac:
Right-click the folder → New Terminal at Folder

2. Run the script
python3 main.py

3. Follow the prompts

You’ll see building numbers:

1. Core Science Facility
2. University Centre
3. Earth Science Building
...


Then select:

Start building

Destination building

Route mode

 Example Output
Route Summary:
1. Library → HKR (tunnel)
2. HKR → The Works (indoor link)

Estimated total travel time: 6.0 minutes