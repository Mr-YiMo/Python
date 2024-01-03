class Node:
    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type  # 'file' or 'dir'
        self.children = []  # 子节点
        self.parent = None  # 父节点

    def __repr__(self):
        return self.name

class FileSystemTree:
    def __init__(self):
        self.root = Node('C:/', 'dir')  # 文件系统的根目录
        self.now = self.root

    # 创建文件夹
    def mkdir(self, filename):
        # name必须以/结尾
        if filename[-1] != '/':
            filename += '/'
        node = Node(filename, 'dir')
        self.now.children.append(node)  # 链接到根目录后
        node.parent = self.now  # 指定返回路径

    # 展示当前目录下的所有目录
    def ls(self):
        return self.now.children

    # 切换目录，只支持一层
    def cd(self,filename):
        if filename[-1] != '/':
            filename += '/'

        if filename == '../':
            self.now = self.now.parent
            return

        for child in self.now.children:
            if child.name == filename:
                self.now = child
                return
        else:
            raise ValueError('invalid dir.')

tree = FileSystemTree()
tree.mkdir('var/')
tree.mkdir('bin/')
tree.mkdir('user/')
print(tree.ls())
tree.cd('bin/')
tree.mkdir('python/')
print(tree.ls())
tree.cd('../')
print(tree.ls())