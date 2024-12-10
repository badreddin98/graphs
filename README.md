# BE Module 12 Lesson 8: Graphs Assignment

This repository contains an implementation of Dijkstra's algorithm for finding the shortest paths in a weighted graph.

## Implementation Details

The solution includes:

1. A `Graph` class that represents a weighted graph using an adjacency list
2. Implementation of Dijkstra's algorithm to find shortest paths
3. Test cases to verify the implementation
4. Time and space complexity analysis

### Time Complexity
- The implementation has a time complexity of O((V + E) log V) where:
  - V is the number of vertices
  - E is the number of edges
  - The log V factor comes from using a priority queue

### Space Complexity
- The space complexity is O(V) for storing:
  - Distances to each vertex
  - Paths to each vertex
  - Priority queue entries

## Running the Code

To run the implementation:

```bash
python dijkstra_algorithm.py
```

The test function will automatically run and display:
1. The graph representation
2. Shortest distances from vertex 'A' to all other vertices
3. The actual shortest paths from vertex 'A' to all other vertices

## Example Output

The test case creates a graph with 5 vertices (A through E) and demonstrates finding the shortest paths from vertex 'A' to all other vertices in the graph.
