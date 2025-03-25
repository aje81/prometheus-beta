import heapq
from typing import Dict, List, Tuple, Optional

def dijkstra(graph: Dict[str, Dict[str, int]], start: str) -> Tuple[Dict[str, int], Dict[str, Optional[str]]]:
    """
    Implement Dijkstra's algorithm to find the shortest paths from a start node.
    
    Args:
        graph (Dict[str, Dict[str, int]]): A graph represented as an adjacency dictionary 
                                           where keys are nodes and values are dictionaries 
                                           of neighboring nodes with their edge weights.
        start (str): The starting node for path calculations.
    
    Returns:
        Tuple containing:
        - A dictionary of shortest distances from the start node to all other nodes
        - A dictionary of previous nodes in the shortest path
    
    Raises:
        ValueError: If the start node is not in the graph
    """
    # Validate input
    if start not in graph:
        raise ValueError(f"Start node '{start}' not found in the graph")
    
    # Initialize distances and previous nodes
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    
    # Priority queue to store nodes to visit
    pq = [(0, start)]
    
    # Track visited nodes to prevent redundant processing
    visited = set()
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Skip if node already processed
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        # Check neighbors
        for neighbor, weight in graph[current_node].items():
            # Calculate potential new distance
            distance = current_distance + weight
            
            # Update if new path is shorter
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, previous_nodes

def reconstruct_path(previous_nodes: Dict[str, Optional[str]], start: str, end: str) -> List[str]:
    """
    Reconstruct the shortest path between start and end nodes.
    
    Args:
        previous_nodes (Dict[str, Optional[str]]): Dictionary of previous nodes in shortest paths
        start (str): The starting node
        end (str): The destination node
    
    Returns:
        List[str]: The shortest path from start to end
    
    Raises:
        ValueError: If no path exists between start and end
    """
    # Validate inputs
    if end not in previous_nodes:
        raise ValueError(f"End node '{end}' not found in the previous nodes dictionary")
    
    path = []
    current = end
    
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
        
        # Prevent infinite loops
        if current == end:
            raise ValueError(f"Circular path detected between {start} and {end}")
    
    # Reverse to get path from start to end
    return list(reversed(path))