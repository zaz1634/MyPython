"""
创建实现一个二叉树的小Demo
要求：
1.节点对象：
属性：
    左孩子节点
    右孩子节点
    节点元素本身
2.树对象：
属性：
    树根
    树队列（用于存储树里的元素）
方法：
    添加元素创建成树
    支持前序遍历（深度优先遍历）
    支持中序遍历
    支持后序遍历
    支持层序遍历（广度优先遍历）

"""


class Node:
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.lchild = lchild
        self.rchild = rchild
        self.elem = elem


class BinaryTree:
    def __init__(self):
        self.root = None
        self.list = []

    def add_Node(self,node:Node):
        if self.root is None:
            self.root=node.elem
            self.list.append(node.elem)
        else:
            self.list.append(node)
            if self.list[0].lchild is None:
                self.list[0].lchild=node
            else:
                self.list[0].rchild=node
                self.list.pop(0)


        pass

if __name__=="__main__":
    tree=BinaryTree()
    for i in range(1,11):
        anode = Node(elem=i)
        tree.add_Node(anode)




    pass











