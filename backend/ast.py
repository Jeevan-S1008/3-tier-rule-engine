class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  
        self.value = value 
        self.left = left 
        self.right = right  
        
    def __repr__(self):
        return f"Node(type={self.type}, value={self.value}, left={self.left}, right={self.right})"
