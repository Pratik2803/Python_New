from linked_list import LinkedList


# Create a new linked list
ll = LinkedList()

# Add elements to the linked list
ll.add_element(10)
ll.add_element(20)
ll.add_element(30)

current = ll.head

print(current.data)
while current.next:
    print(current.next.data)
    current = current.next
