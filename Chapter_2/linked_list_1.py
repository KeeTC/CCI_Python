class Node(object):  # Linked List is defined with THIS function...
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up in order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

def reverse(head):  # Function to reverse the linked list is defined with THIS function
    
    current = head
    previous = None
    nextnode = None
    
    while current:  # While loop
        
        nextnode = current.nextnode  # nextnode = current node of nextnode
        
        current.nextnode = previous # resets nextnode to blank variable
        
        previous = current  # Previous = HEAD, as in the list is now pointing towards the HEAD, not the TAIL
        current = nextnode  # HEAD CAN ONLY BE NEXT NODE IF IT IS RUNNING IN REVERSE!
        
    return previous

reverse(a)

print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)
