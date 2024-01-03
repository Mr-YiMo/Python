class BiTreeNode:
    def __init__(self, data):
        self.data = data  # 节点数据
        self.lchild = None  # 左孩子节点
        self.rchild = None  # 右孩子节点
        self.parent = None


class BiSearchTree:
    def __init__(self, li=None):
        self.root = None
        # 插入传入的列表成员
        if li:
            for val in li:
                # print('2222',val)
                self.insert_no_rec(val)

    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)

        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        else:
            pass  # 已经有的话就啥也不做
        return node

    def insert_no_rec(self, val):
        p = self.root
        if not self.root:  # 空树
            self.root = BiTreeNode(val)
            p = self.root
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:  # 左孩子不存在
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    print(val, '插入', p.lchild.parent.data, '的左子节点')
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:  # 右孩子不存在
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    print(val, '插入', p.rchild.parent.data, '的右子节点')
                    return
            else:
                return

    # 查询
    def query(self, node, val):
        if not node:
            return None
        if node.data < val:
            return self.query(node.rchild, val)
        elif node.data > val:
            return self.query(node.lchild, val)
        else:
            return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            if p.data > val:
                p = p.lchild
            else:
                return p
        return None

    # 情况1:node是叶子节点
    def __remove_node_1(self, node):
        if not node.parent:  # 只有一个节点,并且自己就是根节点
            self.root = None

        # 自己不是根节点清空根节点的子关系
        if node == node.parent.lchild:  # 自己是父亲的左孩子
            node.parent.lchild = None  # 隔断联系
        else:
            node.parent.rchild = None  # 隔断联系

    # 情况21:node是非叶子节点，只有一个左孩子节点
    def __remove_node_21(self, node):
        if not node.parent:  # 只有一个节点,并且自己就是根节点
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:  # 自己是父亲的左孩子
            node.parent.lchild = node.lchild  # 自己左孩子变成自己父亲的左孩子
            node.lchild.parent = node.parent  # 自己左孩子的父亲就是自己的父亲
        else:  # 自己是父亲的右孩子
            node.parent.rchild = node.lchild  # 自己左孩子变成自己父亲的右孩子
            node.lchild.parent = node.parent  # 自己左孩子的父亲就是自己的父亲

    # 情况22:node是非叶子节点，只有一个右孩子节点
    def __remove_node_22(self, node):
        if not node.parent:  # 只有一个节点,并且自己就是根节点
            self.root = node.rchild
            node.rchild.parent = None
        elif node == node.parent.lchild:  # 自己是父亲的左孩子
            node.parent.lchild = node.rchild  # 自己右孩子变成自己父亲的左孩子
            node.rchild.parent = node.parent  # 自己右孩子的父亲就是自己的父亲
        else:  # 自己是父亲的右孩子
            node.parent.rchild = node.rchild  # 自己右孩子变成自己父亲的右孩子
            node.rchild.parent = node.parent  # 自己右孩子的父亲就是自己的父亲

    def delete(self, val):
        if self.root:
            node = self.query_no_rec(val)  # 找到对应节点
            if not node:  # 不存在这个数
                return False
            if not node.lchild and not node.rchild:  # 没有孩子
                self.__remove_node_1(node)
            elif node.lchild and not node.rchild:  # 只有左孩子
                self.__remove_node_21(node)
            elif not node.lchild and node.rchild:  # 只有右孩子
                self.__remove_node_22(node)
            else:  # 有两个孩子,将其右子树的最小节点删除并替换当前节点
                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild # 一直找到最下方的左孩子节点
                node.data = min_node.data #替换数据
                # 删除节点
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)

    # 前序遍历
    def pre_order(self, root):
        if root:
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def mid_order(self, root):
        if root:
            self.mid_order(root.lchild)
            print(root.data, end=',')
            self.mid_order(root.rchild)

    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=',')


def pre_order(root):
    if root:
        print(root.data, end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)


def mid_order(root):
    if root:
        mid_order(root.lchild)
        print(root.data, end=',')
        mid_order(root.rchild)


def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=',')


from collections import deque


def layer_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        # 依次出队
        node = queue.popleft()
        print(node.data, end=',')

        # 将子节点依次进度完毕
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


A = BiTreeNode('A')
B = BiTreeNode('B')
C = BiTreeNode('C')
D = BiTreeNode('D')
E = BiTreeNode('E')
F = BiTreeNode('F')
G = BiTreeNode('G')

E.lchild = A
E.rchild = G
A.lchild = C
C.lchild = B
C.rchild = D
G.rchild = F

'''
        E   
      /   \
    A       G
      \       \
        C       F
       /  \
       B   D
'''

root = E

pre_order(root)
print('')
mid_order(root)
print('')
post_order(root)
print('')
layer_order(root)
print('')

tree = BiSearchTree([17, 5, 35, 2, 11, 29, 38, 9, 8])
tree.pre_order(tree.root)
print('')
tree.mid_order(tree.root)
print('')
tree.post_order(tree.root)
print('')

node = tree.query(tree.root, 17)
print(node.data)
node = tree.query_no_rec(17)
print(node.data)
tree.delete(17)
tree.mid_order(tree.root)