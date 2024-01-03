from abc import abstractmethod,ABCMeta

class Singleton:
    # new中
    def __new__(cls, *args, **kwargs):
        # 用类属性确保类只有一个实例
        if not hasattr(cls,"_instance"): # object的属性，用反射查找cls是否有私有属性_instance
            cls._instance = super(Singleton,cls).__new__(cls) # 调用object类方法开辟一个空间
            return cls._instance

class Myclass(Singleton):
    def __init__(self,num):
        self.num = num
        print('%s create success!' % self.num)


a = Myclass(10) # self.num 已经被创建
b = Myclass(20) # self.num 已经被创建，不会再创建
print(a.num,b.num)


