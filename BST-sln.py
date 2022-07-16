from ctypes.wintypes import PINT


class Node:
    #initializing the Node
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None
    #Inserting Data method
    def insert(self, data):
        array = self.in_order(self)

        if data in array: 
            return
        # Do nothing if no data
        if self.data:
            # Where data value is less than current, branch left
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            # Where data is greater than current, branch right
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
    def in_order(self, root: "Node"):
        """
        Traverse the tree in an 'in order' fashion
        """
        # Create and output container
        output = []
        # Starting at the specified Node, 
        # traverse in Left, Root, Right fashion
        if root:
            # Check Left
            output = self.in_order(root.left)
            # Check Root
            output.append(root.data)
            # Check Right, add output to current output
            output = output + self.in_order(root.right)
        # Returns the list of Nodes in-order
        return output
    def pre_order(self, root: "Node"):
        """
        Traverse the tree in a 'pre-order' fashion
        """
        # Create and output container
        output = []
        # Starting at the specified Node, 
        # traverse in Root, Left, Right fashion 
        if root:
            # Get Root Node Data
            output.append(root.data)

            # Get the Left Node Data and append to current
            output = output + self.pre_order(root.left)
            # Get the Right node data and append to current
            output = output + self.pre_order(root.right)
        # Returns the list of Nodes in pre-order
        return output

    def post_order(self, root: "Node"):
        """
        Traverse the tree in a post-order fashion
        """
        # Create an output container
        output = []
        # Starting at the specified node,
        # Traverse in a left, right, root fashion
        if root:
            # Get left node data
            output = self.post_order(root.left)
            # Get right node data
            output = output + self.post_order(root.right)
            # Get root data
            output.append(root.data)
        # Returns a list of node data in pre-order
        return output
# Create a new Node

# Node Values
data = [13, 5, 23, 4, 6, 22, 28, 3, 3, 27, 32]

# Create the root node from first data item
root = Node(data.pop(0))
# Create and insert Node objects from remaining data
for d in data:
    # Insert a new Node instance
    root.insert(d)

print(root.in_order(root))
print(root.pre_order(root))
print(root.post_order(root))