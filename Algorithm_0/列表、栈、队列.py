# 列表
list = [1, 2, 3, 'sad', 'weq', 46548]


# 栈
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def gettop(self):
        if len(self.stack) > 0:
            return self.stack[-1]  # 列表的最后一个元素
        else:
            return None

    def getlow(self):
        if len(self.stack) > 0:
            return self.stack[0]  # 列表的第一个元素，这里是利用列表实现的，因此时间复杂度只是O(1)
        else:
            return None


# 队列
class Quene:
    def __init__(self, size=100):
        self.quene = [0 for _ in range(size)]  # 最开始时就必须声明长度
        self.rear = 0  # 队尾
        self.front = 0  # 队首
        self.size = size

    def push(self, element):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.size
            self.quene[self.rear] = element
        else:
            raise IndexError('Quene is full.')  # 抛出错误

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.quene[self.front]
        else:
            raise IndexError('Quene is empty.')  # 抛出错误

    def Size(self):
        print('quene size = ', (self.rear - self.front + self.size) % self.size)
        return (self.rear - self.front + self.size) % self.size

    def is_empty(self):
        return self.rear == self.front

    def is_full(self):
        return (self.rear + 1) % self.size == self.front


q = Quene(5)  # 最多存四个
for i in range(4):
    q.push(i)
print(q)
q.pop()
print(q.Size())

# 队列内置模块
from collections import deque

q = deque()  # 空队列

# 单向队列
q.append(1)  # 队尾入队
q.popleft()  # 队首出队

# 双向队列
q.appendleft(1)  # 队首进队
q.pop()  # 队尾出队

# 迷宫问题：栈
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x,y:(x+1,y),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1)
]

def mazpass(x1, y1, x2, y2):
    stack = [(x1, y1)]
    while (len(stack) > 0):
        # 当前的位置
        curNode = stack[-1]

        if curNode[0] == x2 and curNode[1] ==y2:
            # 走到了终点
            for p in stack:
                print(p)
            return  True
        # 上下左右四个方向
        for dir in dirs:
            nextNode = dir(curNode[0],curNode[1])
            # 如果下一个节点能走
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 1 #走过的话将这个路径填上
                break #找到一个能走就返回
        else:
            maze[nextNode[0]][nextNode[1]] = 1 #还是将尝试过的位置标记
            stack.pop()
    else:
        print('No road!')
        return False


# mazpass(1,1,8,8)


def print_r(path):
    curNode = path[-1]
    realpath = []
    while curNode[2] != -1:
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]

    realpath.append(curNode) # 把起点放进去
    realpath.reverse()
    for node in realpath:
        print(node)


from collections import deque
def mazepass_queue(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1,y1,-1)) #开始节点，默认将携带进来的节点记为-1，也就是说path的第一个成员实际为-1
    path = []
    while len(queue) > 0 :
        curNode = queue.popleft() #出队
        path.append(curNode) #保存出队节点信息
        if curNode[0] == x2 and curNode[1] == y2:
            # 终点，输出路径
            print_r(path)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0],curNode[1]) #下一个节点
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0],nextNode[1],len(path)-1)) #下一个节点能走，入队；记录那个节点跳转到它
                maze[nextNode[0]][nextNode[1]] = 1 #标记已经走过
    else:
        print('No read!')
        return False

mazepass_queue(1,1,8,8)