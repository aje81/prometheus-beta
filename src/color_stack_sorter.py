from typing import List, Tuple

class ColorStackSorter:
    """
    A class to sort three stacks of colored balls with specific constraints.
    
    Constraints:
    - Only move one ball at a time between stacks
    - Maintain equal number of balls in each stack
    - Stacks consist of Red, Blue, and Green balls
    """
    
    def __init__(self, red_stack: List[str], blue_stack: List[str], green_stack: List[str]):
        """
        Initialize the color stack sorter with three stacks of balls.
        
        :param red_stack: List of balls in the red stack
        :param blue_stack: List of balls in the blue stack
        :param green_stack: List of balls in the green stack
        """
        self.stacks = {
            'red': red_stack,
            'blue': blue_stack,
            'green': green_stack
        }
        
    def _validate_input(self):
        """
        Validate the initial state of the stacks.
        
        :raises ValueError: If stacks have unequal length or contain invalid colors
        """
        # Check if all stacks have the same length
        stack_lengths = [len(stack) for stack in self.stacks.values()]
        if len(set(stack_lengths)) > 1:
            raise ValueError("All stacks must have equal number of balls")
        
        # Check if all balls are valid colors
        valid_colors = {'red', 'blue', 'green'}
        for stack_name, stack in self.stacks.items():
            for ball in stack:
                if ball.lower() not in valid_colors:
                    raise ValueError(f"Invalid ball color in {stack_name} stack")
    
    def sort(self) -> List[Tuple[str, str, str]]:
        """
        Sort the stacks of colored balls.
        
        :return: List of move tuples (from_stack, to_stack, ball_color)
        :raises ValueError: If sorting is impossible
        """
        # Validate input first
        self._validate_input()
        
        # Track moves
        moves = []
        
        # Continue until each stack has only its own color
        while not self._is_sorted():
            # Find the stack with a ball that needs to be moved
            for from_color, from_stack in self.stacks.items():
                for to_color, to_stack in self.stacks.items():
                    if from_color != to_color and from_stack and from_stack[-1] != from_color:
                        # Move the top ball to the correct stack
                        ball = from_stack.pop()
                        to_stack.append(ball)
                        moves.append((from_color, to_color, ball))
                        break
                
                # Break outer loop if a move was made
                if len(moves) > 0:
                    break
            
            # Prevent infinite loop
            if len(moves) == 0:
                raise ValueError("Unable to sort stacks")
        
        return moves
    
    def _is_sorted(self) -> bool:
        """
        Check if all stacks are sorted (each stack contains only its own color).
        
        :return: True if sorted, False otherwise
        """
        for color, stack in self.stacks.items():
            if any(ball != color for ball in stack):
                return False
        return True