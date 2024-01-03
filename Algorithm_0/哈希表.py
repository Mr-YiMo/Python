class Linklist:
    # 定义节点
    class Node:
        def __init__(self, item=None):
            self.item = item
            self.next = None

    # 定义迭代器
    class LinkListerIterator:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next  # 重新定位下一个节点
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self  # 迭代器的返回值必须是可以迭代的对象

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    # 尾插法
    def append(self, obj):
        s = Linklist.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    # 循环利用尾插法append()将列表保存起来
    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    # 查找函数
    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    # 魔术方法：定义迭代器，利用LinkListerIterator类进行迭代
    def __iter__(self):
        return self.LinkListerIterator(self.head)

    # 魔术方法：重定义输出方式
    def __repr__(self):
        return "<<" + "，".join(map(str, self)) + ">>"


class HashTable:

    def __init__(self, size=101):
        self.size = size  # 定义直接寻址表大小
        self.T = [Linklist() for i in range(self.size)]  # 开直接寻址表，每个表项填入一个链表类

    def h(self, k):
        return k % self.size  # 哈希函数

    def insert(self, k):
        index = self.h(k)  # 查找下标
        if self.find(k):
            print("Duplicate insert.")
        else:
            self.T[index].append(k)

    # 成功查找key = k时，返回 value
    def find(self, k):
        index = self.h(k)
        return self.T[index].find(k)  # 返回值


hashtable = HashTable()
hashtable.insert(0)
hashtable.insert(1)
hashtable.insert(202)  # 会和0在一起

print(",".join(map(str, hashtable.T)))
