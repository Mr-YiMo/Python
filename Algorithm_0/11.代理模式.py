from abc import abstractmethod, ABCMeta


class Object(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self):
        pass


class RealObject(Object):
    def __init__(self,filename):
        self.filename = filename
        f = open(self.filename,mode='r')
        self.content = f.read()
        f.close()

    def get_content(self):
        print('读取文件内容')
        return self.content

    def set_content(self,new_content):
        print('写入文件内容')
        f = open(self.filename,mode='w')
        f.write(new_content)
        f.close()

# 文件很大时候使用虚代理
class VirtualProxy(Object):
    def __init__(self,filename):
        self.filename = filename # 只保存名称，不打开，不占用内存
        self.sub_obj = None

    def get_content(self):
        if not self.sub_obj:
            self.sub_obj = RealObject(self.filename) #开始占用内存建立对象
        return self.sub_obj.get_content()

    def set_content(self,new_content):
        if not self.sub_obj: # 没有实例化先实例化
            self.sub_obj = RealObject(self.filename)  # 开始占用内存建立对象
        return self.sub_obj.set_content(new_content)

# 权限有限制的时候保护代理
class ProtectProxy(Object):
    def __init__(self,filename):
        self.filename = filename # 只保存名称，不打开，不占用内存
        self.sub_obj = RealObject(self.filename)

    # 读权限开放
    def get_content(self):
        return self.sub_obj.get_content()

    # 写权限异常
    def set_content(self,new_content):
        return PermissionError # 权限异常


obj = VirtualProxy("Proxy.txt") # 不创建对象
obj.get_content() # 此时会才创建RealObject对象
print(obj.sub_obj)
obj.set_content('123456') # 此时会才创建RealObject对象
print(obj.get_content())