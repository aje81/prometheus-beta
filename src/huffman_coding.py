from collections import Counter, defaultdict
import heapq

class HuffmanNode:
    """Represents a node in the Huffman tree."""
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        """Allow comparison for heapq sorting."""
        return self.freq < other.freq

def build_frequency_dict(data):
    """
    Build a frequency dictionary for the input data.
    
    Args:
        data (str): Input string to analyze
    
    Returns:
        dict: Character frequency dictionary
    """
    if not data:
        return {}
    return dict(Counter(data))

def build_huffman_tree(freq_dict):
    """
    Build Huffman tree from frequency dictionary.
    
    Args:
        freq_dict (dict): Character frequency dictionary
    
    Returns:
        HuffmanNode: Root of the Huffman tree
    
    Raises:
        ValueError: If frequency dictionary is empty
    """
    if not freq_dict:
        raise ValueError("Frequency dictionary cannot be empty")
    
    # Create heap of nodes
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)
    
    # If only one character, create a dummy node
    if len(heap) == 1:
        node = heap[0]
        dummy = HuffmanNode(None, node.freq)
        dummy.left = node
        return dummy
    
    # Build tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create internal node
        internal = HuffmanNode(None, left.freq + right.freq)
        internal.left = left
        internal.right = right
        
        heapq.heappush(heap, internal)
    
    return heap[0]

def build_huffman_codes(root):
    """
    Generate Huffman codes for each character.
    
    Args:
        root (HuffmanNode): Root of the Huffman tree
    
    Returns:
        dict: Dictionary mapping characters to their Huffman codes
    """
    if not root:
        return {}
    
    codes = {}
    
    def traverse(node, current_code):
        """Recursive helper to generate codes."""
        if not node:
            return
        
        # Leaf node
        if node.char is not None:
            # Special case for single character (to prevent empty code)
            codes[node.char] = "0" if current_code == "" else current_code
            return
        
        # Recursive traversal
        if node.left:
            traverse(node.left, current_code + "0")
        if node.right:
            traverse(node.right, current_code + "1")
    
    traverse(root, "")
    return codes

def huffman_encode(data):
    """
    Encode input data using Huffman coding.
    
    Args:
        data (str): Input string to encode
    
    Returns:
        tuple: (encoded_string, huffman_tree_root)
    
    Raises:
        ValueError: If input is empty
    """
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Special case for single character
    if len(set(data)) == 1:
        return "0" * len(data), build_huffman_tree(build_frequency_dict(data))
    
    # Build frequency dictionary
    freq_dict = build_frequency_dict(data)
    
    # Build Huffman tree
    tree_root = build_huffman_tree(freq_dict)
    
    # Generate Huffman codes
    huffman_codes = build_huffman_codes(tree_root)
    
    # Encode the data
    encoded_data = ''.join(huffman_codes[char] for char in data)
    
    return encoded_data, tree_root

def huffman_decode(encoded_data, tree_root):
    """
    Decode Huffman encoded data.
    
    Args:
        encoded_data (str): Huffman encoded binary string
        tree_root (HuffmanNode): Root of the Huffman tree
    
    Returns:
        str: Decoded original data
    
    Raises:
        ValueError: If encoded data or tree root is invalid
    """
    if not encoded_data and not (tree_root and tree_root.char is not None):
        raise ValueError("Encoded data and tree root must be provided")
    
    # Special case for single character
    if tree_root.left and tree_root.left.char is not None and tree_root.right is None:
        return tree_root.left.char * (len(encoded_data))
    
    decoded_data = []
    current_node = tree_root
    
    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        # Reached a leaf node
        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = tree_root
    
    return ''.join(decoded_data)