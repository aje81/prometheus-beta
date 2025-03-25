import typing

class KnightsTour:
    """
    A class to solve the Knight's Tour problem on an 8x8 chessboard.
    
    The Knight's Tour challenges finding a sequence of knight moves that visits 
    every square exactly once, starting from a given initial position.
    """
    
    def __init__(self, board_size: int = 8):
        """
        Initialize the Knight's Tour solver.
        
        Args:
            board_size (int, optional): Size of the chessboard. Defaults to 8.
        """
        self.board_size = board_size
        self.moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
    
    def is_valid_move(self, x: int, y: int) -> bool:
        """
        Check if the given coordinates are within the board.
        
        Args:
            x (int): X-coordinate
            y (int): Y-coordinate
        
        Returns:
            bool: True if move is within board, False otherwise
        """
        return 0 <= x < self.board_size and 0 <= y < self.board_size
    
    def solve(self, start_x: int, start_y: int) -> typing.Optional[typing.List[typing.Tuple[int, int]]]:
        """
        Solve the Knight's Tour starting from the given position.
        
        Args:
            start_x (int): Starting x-coordinate of the knight
            start_y (int): Starting y-coordinate of the knight
        
        Returns:
            Optional[List[Tuple[int, int]]]: A list of moves forming a complete tour, 
            or None if no solution exists
        """
        # Validate start position
        if not self.is_valid_move(start_x, start_y):
            raise ValueError(f"Invalid starting position: ({start_x}, {start_y})")
        
        # Initialize board tracking
        board = [[-1 for _ in range(self.board_size)] for _ in range(self.board_size)]
        tour = []
        
        def backtrack(x: int, y: int, move_count: int) -> bool:
            """
            Recursive backtracking to find the Knight's Tour.
            
            Args:
                x (int): Current x-coordinate
                y (int): Current y-coordinate
                move_count (int): Number of moves made so far
            
            Returns:
                bool: True if a complete tour is found, False otherwise
            """
            # Mark current square as visited
            board[x][y] = move_count
            tour.append((x, y))
            
            # If all squares are visited, we found a tour
            if move_count == self.board_size * self.board_size - 1:
                return True
            
            # Try all possible knight moves
            for dx, dy in self.moves:
                next_x, next_y = x + dx, y + dy
                
                # Check if the next move is valid and unvisited
                if (self.is_valid_move(next_x, next_y) and 
                    board[next_x][next_y] == -1):
                    if backtrack(next_x, next_y, move_count + 1):
                        return True
            
            # Backtrack: undo the current move if no solution found
            board[x][y] = -1
            tour.pop()
            return False
        
        # Start solving from the given position
        if backtrack(start_x, start_y, 0):
            return tour
        
        return None