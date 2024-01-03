from abc import ABCMeta, abstractmethod

# ------ 抽象产品----------
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass

# --------具体产品----------
class SmallShell(PhoneShell):
    def show_shell(self):
        print("小手机壳")

class BigShell(PhoneShell):
    def show_shell(self):
        print("大手机壳")

# --------抽象工厂---------

class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_Shell(self):
        pass


# ---------具体工厂-----------------
class XiaoMiPhoneFactory(PhoneFactory):
    def make_Shell(self):
        return BigShell()


class HuaWeiPhoneFactory(PhoneFactory):
    def make_Shell(self):
        return SmallShell()


#  -------开始制作----------------

class Phone:
    def __init__(self,shell):
        self.shell = shell

    def show_info(self):
        print('手机信息:')
        self.shell.show_shell()

def make_phone(factory):
    shell = factory.make_Shell()  # 工厂制作手机壳
    return Phone(shell) # 制作好的手机壳保存到手机信息中

p1 = make_phone(HuaWeiPhoneFactory())
p1.show_info()