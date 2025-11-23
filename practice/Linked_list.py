class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None


def reverse_a_linkedlist(head):
    #tranversing to the middle of the doubly linked list
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    beg=slow
    end=fast if fast is not None else None
    while slow:
        beg,end=end,beg
        beg=slow.next
        end=fast.prev
    
    return 
# --- Display the doubly linked list forward ---
def display_list(head):
    current = head
    while current:
        print(current.data, end=" <-> " if current.next else "")
        current = current.next
    print()

# --- Example: build a sample list ---
def build_list(values):
    head = Node(values[0])
    current = head
    for val in values[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = new_node
    return head

# --- Example usage ---
values = [1, 2, 3, 4, 5, 6, 7, 8,9]
head = build_list(values)

print("Original list:")
display_list(head)

# --- Run your function ---
# Assuming your reverse_a_linkedlist returns the (potentially modified) head
# If it doesn't return anything, the list will still be modified in-place
reverse_a_linkedlist(head)
print("Reversed:")
display_list(head)












        

