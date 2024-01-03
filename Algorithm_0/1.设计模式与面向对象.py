from abc import ABCMeta, abstractmethod


# abstract class
class Payment(metaclass=ABCMeta):
    @abstractmethod  # 有抽象方法的类为抽象类
    def pay(self, money):  # interface,规定了A_Pay、B_Pay必须实现这个方法
        pass


class A_Pay(Payment):
    def pay(self, money):
        print("A 支付 %d" % money)


class B_Pay(Payment):
    def pay(self, money):
        print("B 支付 %d" % money)


p = A_Pay()
n = B_Pay()
p.pay(100)
n.pay(100)
