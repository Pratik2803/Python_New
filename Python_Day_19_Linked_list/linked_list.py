from node import Node
from typing import Optional, Any


class LinkedList:

    """
    A class representing a singly linked list.
    Provides functionality to add elements and display the list.
    """

    def __init__(self) -> None:
        """
        Initialize an empty singly linked list.
        """
        self.head: Optional[Node] = None

    def add_element(self, data: Any) -> None:
        """
        Add a new element to the end of the linked list.

        Args:
            data (Any): The data to store in the new node.
        """

        new_node = Node(data)  # Create a new node
        if not self.head:
            # If the list is empty, set the new node as the head
            self.head = new_node

        else:
            # Traverse to the last node
            last = self.head
            while last.next:
                last = last.next

            # Link the last node to the new node
            last.next = new_node
