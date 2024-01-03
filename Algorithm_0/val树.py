from 二叉树 import BiTreeNode, BiSearchTree

class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self,data)
        self.bf = 0  # balanace factor


class AVLTree(BiSearchTree):
    def __init__(self, li=None):
        BiSearchTree.__init__(self, li)

        # 情况一
    def rotate_left(self, p, c):
        # s2移到p的右子节点
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p

        # p移到c的左子节点
        c.lchild = p
        p.parent = c

        # 更新balance factor
        p.bf = 0  # p已经平衡
        c.bf = 0  # c已经平衡
        return c

    # 情况二
    def rotate_right(self, p, c):
        # s2移到p的左子节点
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p

        # p移到c的左子节点
        c.rchild = p
        p.parent = c

        # 更新balance factor
        p.bf = 0  # p已经平衡
        c.bf = 0  # c已经平衡
        return c

    # 情况三
    def rotate_right_left(self, p, c):
        g = c.lchild
        # 将g的左孩子给p的右孩子节点,，将p挪到g的左孩子节点
        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        # 将g的右孩子给c的左孩子节点，将c挪到g的右孩子节点
        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        # 更新balance factor
        if g.bf > 0:  # 说明原本S3上有数据，k接着插入到s3
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:  # 说明k插到s2
            p.bf = 0
            c.bf = 1
        else:  # 插入的是g
            p.bf = 0
            c.bf = 0
        g.bf = 0
        return g

    # 情况四
    def rotate_left_right(self, p, c):
        g = c.rchild
        # 将g的左孩子给c的右孩子节点,，将c挪到g的左孩子节点
        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g

        # 将g的右孩子给p的左孩子节点，将p挪到g的右孩子节点
        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        # 更新balance factor
        if g.bf > 0:  # 说明k插到s3
            p.bf = 0
            c.bf = -1
        elif g.bf < 0:  # 说明k插到s2
            p.bf = 1
            c.bf = 0
        else:  # 插入的是g
            p.bf = 0
            c.bf = 0
        g.bf = 0
        return g

    # 覆盖父类的方法
    def insert_no_rec(self, val):
        # 和二叉搜索树，先插入
        p = self.root
        if not self.root:  # 空树
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:  # 左孩子不存在
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p
                    node = p.lchild  # 保存插入的节点
                    print(val, 'val插入', p.lchild.parent.data, '的左子节点')
                    break  # 结束插入，不能return，因为后续还要旋转
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:  # 右孩子不存在
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild  # 保存插入的节点
                    print(val, 'val插入', p.rchild.parent.data, '的右子节点')
                    break
            else:
                return # 没有插入可以不调整

        # 更新balance factor，从node的parent开始
        while node.parent: # node的parent存在
            if node.parent.lchild == node: #传递是从左子树来的，左子树更沉了
                # 更新node.parent.bf
                if node.parent.bf < 0:
                    # 看node那边沉，进行旋转
                    g = node.parent.parent # 为了链接用
                    x = node.parent # 旋转前的子树的根
                    if node.bf > 0:
                        print("rotate_left_right")
                        n = self.rotate_left_right(node.parent,node)
                    else:
                        print("rotate_right")
                        n = self.rotate_right(node.parent,node)
                    # 链接g和n
                elif node.parent.bf > 0:# 原来的是1，插入到了左边，bf不变
                    node.parent.bf = 0
                    break
                else:
                    node.parent.bf = -1
                    node = node.parent  # 继续走循环
                    continue
            else:  # 从右子树来的，右子树更沉了
                if node.parent.bf >0:
                    g = node.parent.parent  # 为了链接用
                    x = node.parent # 旋转前的子树的根
                    if node.bf < 0:
                        print("rotate_right_left")
                        n = self.rotate_right_left(node.parent, node)
                    else:
                        print("rotate_left")
                        n = self.rotate_left(node.parent, node)
                    # 链接g和n
                elif node.parent.bf < 0:  # 原来的是-1，插入到了右边，bf不变
                    node.parent.bf = 0
                    break
                else:
                    node.parent.bf = 1
                    node = node.parent  # 继续走循环
                    continue
            # 链接旋转后的子树，g与n链接起来
            n.parent = g
            if g:
                if x == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break
            else:
                self.root = n
                break

print("------------AVL--------------")
tree = AVLTree([9,8,7,6,5,4,3,2,1])
tree.pre_order(tree.root)
print("")
tree.mid_order(tree.root)
