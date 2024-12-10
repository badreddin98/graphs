"""
BE Module 12 Lesson 8: Assignment | Graphs
Implementation of Dijkstra's Algorithm for finding shortest paths in a weighted graph
"""

from collections import defaultdict
import heapq

class Graph:
    def __init__(self):
        """Initialize an empty graph using dictionary to store vertices and their neighbors"""
        self.vertices = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph if it doesn't exist"""
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, source, destination, weight):
        """Add a weighted edge between source and destination vertices"""
        if source in self.vertices and destination in self.vertices:
            self.vertices[source][destination] = weight
            self.vertices[destination][source] = weight  # For undirected graph

    def get_neighbors(self, vertex):
        """Get all neighbors of a vertex with their weights"""
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return {}

    def dijkstra(self, start_vertex):
        """
        Implement Dijkstra's algorithm to find shortest paths from start_vertex to all other vertices
        
        Time Complexity: O((V + E) log V) where V is number of vertices and E is number of edges
        Space Complexity: O(V) for storing distances and paths
        """
        # Initialize distances dictionary with infinity for all vertices except start
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start_vertex] = 0
        
        # Dictionary to store the path to each vertex
        paths = {vertex: [] for vertex in self.vertices}
        paths[start_vertex] = [start_vertex]
        
        # Priority queue to store vertices and their distances
        pq = [(0, start_vertex)]
        
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            
            # If we've found a longer path, skip
            if current_distance > distances[current_vertex]:
                continue
                
            # Check all neighbors of current vertex
            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                
                # If we've found a shorter path, update it
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    paths[neighbor] = paths[current_vertex] + [neighbor]
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances, paths

def test_dijkstra_algorithm():
    """Test function to verify the implementation"""
    # Create a test graph
    graph = Graph()
    
    # Add vertices
    vertices = ['A', 'B', 'C', 'D', 'E']
    for vertex in vertices:
        graph.add_vertex(vertex)
    
    # Add edges
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 8)
    graph.add_edge('C', 'E', 10)
    graph.add_edge('D', 'E', 2)
    
    # Test the graph representation
    print("\nGraph representation:")
    print(graph.vertices)
    
    # Find shortest paths from vertex 'A'
    distances, paths = graph.dijkstra('A')
    
    # Print results
    print("\nShortest distances from vertex 'A':")
    for vertex in distances:
        print(f"To {vertex}: {distances[vertex]}")
    
    print("\nShortest paths from vertex 'A':")
    for vertex in paths:
        print(f"To {vertex}: {' -> '.join(paths[vertex])}")

if __name__ == "__main__":
    # Run the test
    test_dijkstra_algorithm()
