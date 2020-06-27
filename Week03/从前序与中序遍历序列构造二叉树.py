#根据一棵树的前序遍历和中序遍历构造二叉树
#首先定义二叉树结构
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
class Solution:
    def buildTree(self,preorder:list,inorder:list):
        def myBuildTree(preorder_left:int,preorder_right:int,inorder_left:int,inorder_right:int):
            if preorder_left>preorder_right:
                return None
            # 前序遍历中的第一个节点就是根节点
            preorder_root=preorder_left
            # 在中序遍历中定位根节点
            inorder_root=inorder.index(preorder[preorder_root])
            # 先把根节点建立出来
            root=TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree=inorder_root-inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left=myBuildTree(preorder_left+1,preorder_left+size_left_subtree,inorder_left,inorder_root-1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left+size_left_subtree+1,preorder_right,inorder_root+1,inorder_right)
            return root
        if len(preorder) !=len(inorder):
            return None
        return myBuildTree(0,len(preorder)-1,0,len(preorder)-1)
p=[3,9,20,15,7]
m=[9,3,15,20,7]
x=Solution()
x.buildTree(p, m)
