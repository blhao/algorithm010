# 二叉树的最近公共祖先
# 首先定义二叉树类
class treeNode:
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None


class binaryTree:
    def __init__(self, node=None):
        self.root = node
    # 增加节点

    def add(self, item):
        if self.root == None:
            self.root = treeNode(item)
        else:
            queue = list()
            queue.append(self.root)
            while len(queue) > 0:
                node = queue.pop(0)
                if not node.lchild:
                    node.lchild = treeNode(item)
                    return
                else:
                    queue.append(node.lchild)
                if not node.rchild:
                    node.rchild = treeNode(item)
                    return
                else:
                    queue.append(node.rchild)
    # 广度优先遍历查找某个节点

    def breadh_travel_search(self, data):
        if self.root == None:
            return []
        if self.root.item == data:
            return root
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop(0)
            if node.lchild:
                if node.lchild.item == data:
                    return node.lchild
                queue.append(node.lchild)
            if node.rchild:
                if node.rchild.item == data:
                    return node.rchild
                queue.append(node.rchild)
# 具体思路：
# （1） 如果当前结点 rootroot 等于 NULL，则直接返回 NULL
# （2） 如果 rootroot 等于 pp 或者 qq ，那这棵树一定返回 pp 或者 qq
# （3） 然后递归左右子树，因为是递归，使用函数后可认为左右子树已经算出结果，用 leftleft 和 rightright 表示
# （4） 此时若leftleft为空，那最终结果只要看 rightright；若 rightright 为空，那最终结果只要看 leftleft
# （5） 如果 leftleft 和 rightright 都非空，因为只给了 pp 和 qq 两个结点，都非空，说明一边一个，因此 rootroot 是他们的最近公共祖先


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.lchild, p, q)
        right = self.lowestCommonAncestor(root.rchild, p, q)
        if not left:
            return right
        if not right:
            return left
        return root


if __name__ == '__main__':
    tree = binaryTree()
    tree.add(3)
    tree.add(5)
    tree.add(1)
    tree.add(6)
    tree.add(2)
    tree.add(0)
    tree.add(8)
    tree.add(7)
    tree.add(4)
    root = tree.root
    p = tree.breadh_travel_search(5)
    q = tree.breadh_travel_search(4)
    S = Solution()
    result = S.lowestCommonAncestor(root, p, q)
    print(result.item)
