class DisjointSet:
    """
    Disjoint Set (Union-Find) data structure to help with Kruskal's algorithm.
    
    This class provides efficient methods to detect cycles and connect components
    while finding the minimum spanning tree.
    """
    def __init__(self, vertices):
        """
        Initialize the disjoint set with each vertex in its own set.
        
        :param vertices: Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, item):
        """
        Find the root of a given vertex with path compression.
        
        :param item: Vertex to find the root for
        :return: Root of the vertex
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        """
        Union of two sets by rank.
        
        :param x: First vertex
        :param y: Second vertex
        :return: Boolean indicating if union was successful
        """
        x_root = self.find(x)
        y_root = self.find(y)

        # If roots are same, this would create a cycle
        if x_root == y_root:
            return False

        # Union by rank
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

        return True

def kruskal_mst(graph):
    """
    Implement Kruskal's algorithm to find Minimum Spanning Tree.
    
    :param graph: List of edges, where each edge is (weight, u, v)
    :return: List of edges in the minimum spanning tree
    :raises ValueError: If graph is invalid or cannot form a spanning tree
    """
    # Input validation
    if not graph:
        raise ValueError("Graph cannot be empty")

    # Sort edges by weight
    graph = sorted(graph, key=lambda x: x[0])

    # Get number of vertices
    vertices = max(max(u, v) for _, u, v in graph) + 1

    # Initialize Disjoint Set
    ds = DisjointSet(vertices)
    mst = []

    # Process sorted edges
    for weight, u, v in graph:
        # If including this edge doesn't create a cycle, add it
        if ds.union(u, v):
            mst.append((weight, u, v))

    # Verify MST covers all vertices
    if len(mst) != vertices - 1:
        raise ValueError("Graph is not fully connected")

    return mst