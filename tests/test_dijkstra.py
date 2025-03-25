import pytest
from src.dijkstra import dijkstra, reconstruct_path

def test_dijkstra_basic_graph():
    """Test Dijkstra's algorithm on a simple graph."""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    
    distances, previous = dijkstra(graph, 'A')
    
    assert distances == {
        'A': 0,
        'B': 3,  # A -> C -> B
        'C': 2,  # A -> C
        'D': 6   # A -> C -> B -> D
    }
    
    # Test path reconstruction
    assert reconstruct_path(previous, 'A', 'D') == ['A', 'C', 'B', 'D']

def test_dijkstra_single_node_graph():
    """Test Dijkstra's algorithm with a single node graph."""
    graph = {'A': {}}
    
    distances, previous = dijkstra(graph, 'A')
    
    assert distances == {'A': 0}
    assert previous == {'A': None}

def test_dijkstra_invalid_start_node():
    """Test handling of invalid start node."""
    graph = {'A': {'B': 1}, 'B': {}}
    
    with pytest.raises(ValueError, match="Start node 'C' not found in the graph"):
        dijkstra(graph, 'C')

def test_reconstruct_path_no_path():
    """Test path reconstruction when no path exists."""
    previous = {'A': None, 'B': 'A', 'C': 'B'}
    
    with pytest.raises(ValueError, match="End node 'D' not found"):
        reconstruct_path(previous, 'A', 'D')

def test_dijkstra_disconnected_graph():
    """Test Dijkstra's algorithm on a disconnected graph."""
    graph = {
        'A': {'B': 1},
        'B': {'A': 1},
        'C': {'D': 2},
        'D': {'C': 2}
    }
    
    distances, previous = dijkstra(graph, 'A')
    
    assert distances['A'] == 0
    assert distances['B'] == 1
    assert distances['C'] == float('inf')
    assert distances['D'] == float('inf')

def test_reconstruct_path_basic():
    """Test basic path reconstruction."""
    previous = {
        'A': None,
        'B': 'A',
        'C': 'B',
        'D': 'C'
    }
    
    path = reconstruct_path(previous, 'A', 'D')
    assert path == ['A', 'B', 'C', 'D']