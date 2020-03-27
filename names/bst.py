class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value < self.value look left
        if value < self.value:
            # if something is there already
            if self.left:
                # recurse left
                self.left.insert(value)
            # if not
            else:
                # insert left
                self.left = BinarySearchTree(value)

        # if value >= self.value look right
        if value >= self.value:
            # if something is there already
            if self.right:
                # recurse right
                self.right.insert(value)
            # if not
            else:
                # insert right
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not

    # if node is none:
    #  return false
    # if node.value == findvalue:
        # return true
    # else:
    #      if find < node.value:
              # find on left node
         # else
            # find on right node

    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
