class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
        self.prior =None

# 头插法
def Head_insert(li):
    head = Node(li[0]) #插入头
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head

def print_linklist(lk):
    while lk != None:
        print(lk.item,end = ',')
        lk = lk.next

hd  = Head_insert([1,2,3])
print_linklist(hd)

# 尾插法
def Tail_insert(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head

hd1  = Tail_insert([1,2,3])
print_linklist(hd1)