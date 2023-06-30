Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.

CODE:
from collections import deque

class Solution:
    def topoSort(self, V, adj):
        # Initialize an array to store the in-degree of each vertex
        in_degree = [0] * V

        # Calculate the in-degree of each vertex
        for u in range(V):
            for v in adj[u]:
                in_degree[v] += 1

        # Create a queue to store the vertices with in-degree 0
        queue = deque()

        # Add the vertices with in-degree 0 to the queue
        for i in range(V):
            if in_degree[i] == 0:
                queue.append(i)

        # Initialize a list to store the topological ordering
        topo_order = []

        # Perform topological sorting
        while queue:
            u = queue.popleft()
            topo_order.append(u)

            # Decrease the in-degree of adjacent vertices
            for v in adj[u]:
                in_degree[v] -= 1

                # If the in-degree becomes 0, add the vertex to the queue
                if in_degree[v] == 0:
                    queue.append(v)

        return topo_order
