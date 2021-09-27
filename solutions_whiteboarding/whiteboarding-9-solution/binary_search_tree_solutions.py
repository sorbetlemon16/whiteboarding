class BinarySearchNode(object):
    """Binary tree node."""

    def __init__(self, data, left=None, right=None):
        self.data = data

        self.left = left
        self.right = right

    def __repr__(self):
        """Debugging-friendly representation."""

        return "<BinaryNode %s>" % self.data

    def find_iterative(self, sought):
        """Return node with this data.

        Start here. Return None if not found.

        >>> root_left_left_left = BinarySearchNode(1)
        >>> root_left_left = BinarySearchNode(2, root_left_left_left)
        >>> root_left_right = BinarySearchNode(4)
        >>> root_left = BinarySearchNode(3, root_left_left, root_left_right)
        >>> root_right_right_left = BinarySearchNode(8)
        >>> root_right_right_right = BinarySearchNode(10)
        >>> root_right_left = BinarySearchNode(6)
        >>> root_right_right = BinarySearchNode(9,root_right_right_left, root_right_right_right)
        >>> root_right = BinarySearchNode(7, root_right_left, root_right_right)
        >>> root_node = BinarySearchNode(5, root_left, root_right)
        >>> root_node.find_iterative(7)
        <BinaryNode 7>
        >>> root_node.find_iterative(11) is None
        True
        >>> root_node.find_iterative(0) is None
        True
        """

        current = self

        while current:
            if current.data == sought:
                return current

            elif sought < current.data:
                current = current.left

            elif sought > current.data:
                current = current.right

        return None

    def find_recursive(self, sought):
        """Return node with this data.

        Start here. Return None if not found.

        >>> root_left_left_left = BinarySearchNode(1)
        >>> root_left_left = BinarySearchNode(2, root_left_left_left)
        >>> root_left_right = BinarySearchNode(4)
        >>> root_left = BinarySearchNode(3, root_left_left, root_left_right)
        >>> root_right_right_left = BinarySearchNode(8)
        >>> root_right_right_right = BinarySearchNode(10)
        >>> root_right_left = BinarySearchNode(6)
        >>> root_right_right = BinarySearchNode(9,root_right_right_left, root_right_right_right)
        >>> root_right = BinarySearchNode(7, root_right_left, root_right_right)
        >>> root_node = BinarySearchNode(5, root_left, root_right)
        >>> root_node.find_recursive(7)
        <BinaryNode 7>
        >>> root_node.find_recursive(11) is None
        True
        >>> root_node.find_recursive(0) is None
        True
        """

        if self.data == sought:
            return self
        elif sought < self.data and self.left is not None:
            return self.left.find_recursive(sought)
        elif sought > self.data and self.right is not None:
            return self.right.find_recursive(sought)
        else:
            return None

    def insert_iterative(self, data):
        """Insert node in its right spot, assuming there are no ties.

        Note: this is not optimized and will not keep the tree balanced.

        >>> root_left_left = BinarySearchNode(1, None)
        >>> root_left_right = BinarySearchNode(4)
        >>> root_left = BinarySearchNode(3, root_left_left, root_left_right)
        >>> root_right_right_left = BinarySearchNode(8)
        >>> root_right_right_right = BinarySearchNode(10)
        >>> root_right_right = BinarySearchNode(9,root_right_right_left, root_right_right_right)
        >>> root_right = BinarySearchNode(7, None, root_right_right)
        >>> root_node = BinarySearchNode(5, root_left, root_right)
        >>> root_node.insert_recursive(11)
        >>> root_node.right.right.right.right
        <BinaryNode 11>
        >>> root_node.insert_recursive(6)
        >>> root_node.right.left
        <BinaryNode 6>
        >>> root_node.insert_recursive(2)
        >>> root_node.left.left
        <BinaryNode 1>
        >>> root_node.left.left.right
        <BinaryNode 2>
        """

        current = self

        to_insert = BinarySearchNode(data, None, None)

        while True:

            # print "checking ", current.data

            if current.right and data > current.right:
                # If we're bigger than the right node, descend into it
                current = current.right
            elif current.left and data < current.left:
                # If we're smaller than the left node, descend into it
                current = current.left
            elif data > current:
                # If we're bigger than the parent, insert node as its right
                # child (we already know we are smaller than the right child
                # if it exists at all)
                to_insert.right = current.right
                current.right = to_insert
                return
            else:
                # The remaining scenario: we are smaller than the parent,
                # but larger than the left child if it exists:
                to_insert.left = current.left
                current.left = to_insert
                return

    def insert_recursive(self, data):
        """Insert new node with `new_data` to BST tree rooted here.

        >>> root_left_left = BinarySearchNode(1, None)
        >>> root_left_right = BinarySearchNode(4)
        >>> root_left = BinarySearchNode(3, root_left_left, root_left_right)
        >>> root_right_right_left = BinarySearchNode(8)
        >>> root_right_right_right = BinarySearchNode(10)
        >>> root_right_right = BinarySearchNode(9,root_right_right_left, root_right_right_right)
        >>> root_right = BinarySearchNode(7, None, root_right_right)
        >>> root_node = BinarySearchNode(5, root_left, root_right)
        >>> root_node.insert_recursive(11)
        >>> root_node.right.right.right.right
        <BinaryNode 11>
        >>> root_node.insert_recursive(6)
        >>> root_node.right.left
        <BinaryNode 6>
        >>> root_node.insert_recursive(2)
        >>> root_node.left.left
        <BinaryNode 1>
        >>> root_node.left.left.right
        <BinaryNode 2>
        """

        if data >= self.data:
            if self.right is None:
                self.right = BinarySearchNode(data)
            else:
                self.right.insert_recursive(data)
        else:
            if self.left is None:
                self.left = BinarySearchNode(data)
            else:
                self.left.insert_recursive(data)

    def count_total_nodes_iterative(self):
        """Count the overal number of nodes

        >>> root_left_left_left = BinarySearchNode(1)
        >>> root_left_left = BinarySearchNode(2, root_left_left_left)
        >>> root_left_right = BinarySearchNode(4)
        >>> root_left = BinarySearchNode(3, root_left_left, root_left_right)
        >>> root_right_right_left = BinarySearchNode(8)
        >>> root_right_right_right = BinarySearchNode(10)
        >>> root_right_left = BinarySearchNode(6)
        >>> root_right_right = BinarySearchNode(9,root_right_right_left, root_right_right_right)
        >>> root_right = BinarySearchNode(7, root_right_left, root_right_right)
        >>> root_node = BinarySearchNode(5, root_left, root_right)
        >>> total = root_node.count_total_nodes_iterative()
        >>> total == 10
        True
        """

        # This code is essentially an iterative BFS traversal, but we have to
        # do a slightly more complex version of to_visit.extend()
        if self is None:
            return 0

        count = 0

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()
            count += 1
            if current.left is not None:
                to_visit.append(current.left)
            if current.right is not None:
                to_visit.append(current.right)

        return count

    def count_total_nodes_recursive(self):
        """Count the overal number of nodes


        >>> root_left_left_left = BinarySearchNode(1)
        >>> root_left_left = BinarySearchNode(2, root_left_left_left)
        >>> root_left_right = BinarySearchNode(4)
        >>> root_left = BinarySearchNode(3, root_left_left, root_left_right)
        >>> root_right_right_left = BinarySearchNode(8)
        >>> root_right_right_right = BinarySearchNode(10)
        >>> root_right_left = BinarySearchNode(6)
        >>> root_right_right = BinarySearchNode(9,root_right_right_left, root_right_right_right)
        >>> root_right = BinarySearchNode(7, root_right_left, root_right_right)
        >>> root_node = BinarySearchNode(5, root_left, root_right)
        >>> total = root_node.count_total_nodes_recursive()
        >>> total == 10
        True
        """

        # Count nodes in left subtree:
        if self.left is None:
            left_total = 0
        else:
            left_total = self.left.count_total_nodes_recursive()
        
        # Count nodes in right subtree:
        if self.right is None:
            right_total = 0
        else:
            right_total = self.right.count_total_nodes_recursive()

        # Total number of nodes in tree is current node plus sizes of left
        # and right subtrees
        return 1 + left_total + right_total
