class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
class AVL_Tree(object):
    def insert(self, root, data):
        if not root:
            return TreeNode(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)
        #  Case 1 - left left
        if balance > 1 and data < root.left.data:
            return self.rightRotate(root)
        # Case 2 - right right
        if balance < -1 and data > root.right.data:
            return self.leftRotate(root)
        # case 3 - left rotate
        if balance > 1 and data > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # case 4 - right rotate
        if balance < -1 and data < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

    def leftRotate(self, z):
        y = z.right
        t2 = y.left

        y.left = z
        z.right = t2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, y):
        z = y.left
        t2 = z.right

        z.right = y
        y.left = t2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return z

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def delete(self, root, key):

        # Step 1 - Perform standard BST delete
        if not root:
            return root

        elif key < root.data:
            root.left = self.delete(root.left, key)

        elif key > root.data:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right,temp.val)

            if root is None:
                return root

            root.height = 1+ max(self.getHeight(root.left),self.getHeight(root.right))

            balance = self.getBalance(root)
            #case1 left left

            if balance > 1 and self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            #case2 right right
            if balance < -1 and self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            #case3 left right
            if balance > 1 and self.getBalance(root.left) < 0:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
            #case4 right left
            if balance < -1 and self.getBalance(root.right) > 0:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

            return root

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root

        return self.getMinValueNode(root.left)

    def inOrder(self, root):

        if not root:
            return

        self.inOrder(root.left)
        print("{0} ".format(root.data), end="")
        self.inOrder(root.right)


myTree = AVL_Tree()
root = None
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for num in nums:
    root = myTree.insert(root, num)

print("Inorder Traversal after insertion -")
myTree.inOrder(root)
print()

root = myTree.delete(root, 10)

print("Inorder Traversal after insertion -")
myTree.inOrder(root)
print()