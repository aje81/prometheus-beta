import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set():
    """Test Disjoint Set (Union-Find) data structure."""
    ds = DisjointSet(5)
    
    # Initially, each vertex is in its own set
    assert ds.find(0) != ds.find(1)
    
    # Union two sets
    ds.union(0, 1)
    assert ds.find(0) == ds.find(1)
    
    # Subsequent unions
    ds.union(1, 2)
    assert ds.find(0) == ds.find(2)

def test_kruskal_mst_basic():
    """Test Kruskal's algorithm with a simple connected graph."""
    # Graph: [(weight, u, v), ...]
    graph = [
        (4, 0, 1),
        (8, 0, 7),
        (11, 1, 7),
        (8, 1, 2),
        (7, 7, 8),
        (1, 7, 6),
        (2, 8, 6),
        (6, 2, 8),
        (2, 2, 5),
        (4, 2, 3),
        (7, 3, 5),
        (14, 3, 4),
        (9, 5, 6),
        (10, 4, 5)
    ]
    
    mst = kruskal_mst(graph)
    
    # Verify MST properties
    assert len(mst) == 6  # For a graph with 9 vertices, MST has 8 vertices - 1 edges
    
    # Calculate total MST weight
    total_weight = sum(weight for weight, _, _ in mst)
    assert total_weight == 37  # Expected minimal spanning tree weight

def test_kruskal_mst_single_edge():
    """Test MST with a graph having only one edge."""
    graph = [(5, 0, 1)]
    mst = kruskal_mst(graph)
    assert mst == [(5, 0, 1)]

def test_kruskal_mst_invalid_input():
    """Test error handling for invalid inputs."""
    # Empty graph
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        kruskal_mst([])

def test_kruskal_mst_disconnected_graph():
    """Test error handling for disconnected graph."""
    # Disconnected graph
    graph = [
        (1, 0, 1),
        (2, 2, 3)
    ]
    with pytest.raises(ValueError, match="Graph is not fully connected"):
        kruskal_mst(graph)

def test_kruskal_mst_cycle_prevention():
    """Ensure Kruskal's algorithm prevents cycles."""
    graph = [
        (1, 0, 1),
        (2, 1, 2),
        (3, 2, 0)  # This edge would create a cycle
    ]
    
    mst = kruskal_mst(graph)
    
    # Only two edges should be in MST
    assert len(mst) == 2
    
    # Verify the edges are the minimal ones
    assert sorted((1, 0, 1)) in sorted(mst)
    assert sorted((2, 1, 2)) in sorted(mst)
    assert sorted((3, 2, 0)) not in sorted(mst)