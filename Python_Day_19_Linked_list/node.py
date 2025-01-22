from typing import Optional


class Node:

    """
    Represents a single node in a singly linked list.
    Each node contains data and a reference to the next node.
    """

    def __init__(self, data: any) -> None:
        """
        Initialize a node with the given data.

        Args :
            data(any) : The data to store in the node.
        """
        self.data = data
        # Reference to the next node defaults to None
        self.next: Optional[Node] = None
