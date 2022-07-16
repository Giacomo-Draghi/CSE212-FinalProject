# Binary Search Tree

Binary Search tree, also known as **BST**, is a non-linear data structure, is can be defined as a rooted binary tree data structure with the key of each internal node being greater than all the keys in the respective node's left subtree and less than the ones in its right subtree. The time complexity of operations on the binary search tree is directly proportional to the height of the tree.

In other words, when looking at a BST, we are looking kind of like a genealogy tree, where the further you gon on the roots, the logest it gets to find something, on a big O notation, searching a BST is O(log *n*).

## Using BST

In other words to build up a BST we need to work with a **Node** class, and also we will need the ability to **insert** new nodes, in order to do that we need to start looking at the Nodes fisrt. 

In the following immage we can see the classic structure of a BST, composed tipically of 3 elements: 
1. *Parent*, that is the node from witch all other nodes follow
2. *Left child*, the node to the left of the parent
3. *Right child*, the node to the right of the parent

![Alternate Text to Display](https://www.alpharithms.com/wp-content/uploads/2268/node-class-basics.jpg)

So we can start looking at the BST by creating the node class and initializing it like so: 

```python
class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None
        
# Create a new Node
node_one = Node(1)
```

### Insert
Now that we started by creating the first Node, we need to start plaing aroung with some values and start to insert some child nodes. 

![Alternate Text to Display](https://www.alpharithms.com/wp-content/uploads/2268/bst-insert-node-algorithm-illustration-alpharithms.jpg)

To do so, it is a best practice to follow some steps. 
1. Check if there is any data
2. If that data is less than the current node’s data
    - If no existing reference to a left Node, add as a new reference
    - If an existing left Node reference exists, insert into that Node
3. If that data is greater than the current Node’s data
    - If no existing reference to a right Node, add as a new reference
    - If an existing right Node reference exists, insert into that Node
 like so: 
```python
    def insert(self, data):
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
# Create a new Node
node_one = Node(1)
node_one.insert(5)
print(node_one.right.data) #Result: 5
```
## Traveling BST

Now that we created the BST and are more confident with the structure, we need to start looking at the tree, and to do some example we can look at traversing the BST. This can be done in different ways: 

1. in-order
2. pre-order
3. post-order

![Alternate Text to Display](https://www.alpharithms.com/wp-content/uploads/2268/binary-search-tree-traversal-types-alpharithms.jpg)

Here it follows some example of the 3 different ways tro traverse the BST: 

### In-Order

```python
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
```
### Pre-Order 
```python
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
```
### Post-Order
```python
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
```

## Problem Solve: Adding and Searching a BST

Now that we had a chance to build some BST and know how to traverse it, we need to do some practice. The exercise is simple, given the following set of values: `data = [13, 5, 23, 4, 6, 22, 28, 3, 3, 27, 32]` you need to add it in a BST and if the value is already present anywhere in the tree, then you should not insert it. 

At the end, print the BST as a list of all the value in the 3 different ways of traversing the BST. 

[Back to Homepage](Home)

You can find a solution example here: [Solution](BST-sln.py) 