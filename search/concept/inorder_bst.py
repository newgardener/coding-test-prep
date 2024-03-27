class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class InOrderBst:
    def minDiffInBst(self, root):
        node = root
        if node is not None:
            self.minDiffInBst(node.left)
            self.inOrderNodeList.append(node.val)
            self.minDiffInBst(node.right)

    def calcMinDiff(self, root):
        self.inOrderNodeList = []
        self.minDiffInBst(root)
        min_diff = float("inf")
        for i in range(len(self.inOrderNodeList) - 1):
            min_diff = min(
                abs(self.inOrderNodeList[i + 1] - self.inOrderNodeList[i]), min_diff
            )
        return min_diff


if __name__ == "__main__":
    example = TreeNode(4)
    example.left = TreeNode(2)
    example.left.left = TreeNode(1)
    example.left.right = TreeNode(3)
    example.right = TreeNode(6)

    example2 = TreeNode(40)
    example2.right = TreeNode(70)
    example2.right.left = TreeNode(50)
    example2.right.right = TreeNode(90)

    inOrderBst = InOrderBst()
    print(inOrderBst.calcMinDiff(example))
    print(inOrderBst.calcMinDiff(example2))
