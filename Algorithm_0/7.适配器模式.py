from abc import ABCMeta, abstractmethod

# abstract class
class Payment(metaclass=ABCMeta):
    @abstractmethod  # 有抽象方法的类为抽象类
    def pay(self, money):
        pass


class AliPay(Payment):
    def pay(self, money):
        print("支付宝 支付 %d" % money)


class WeChatPay(Payment):
    def pay(self, money):
        print("微信 支付 %d" % money)


class MastercardPay:
    def cost(self,money): # 名字不一样，如何之前一样调用pay(self, money)实现呢？
        print("信用卡 支付 %d" % money)


# 继承实现,客户端后续统一调用MastercardPay_Adapter类
class MastercardPay_Adapter1(Payment,MastercardPay):
    def pay(self, money):
        self.cost(money) # 即实现接口统一

# 组合实现
class MastercardPay_Adapter2:
    def __init__(self,payment):
        self.payment = payment

    def pay(self, money):
        # 如果有多个不同的类，可以使用类名，if elif进行区分即可
        self.payment.cost(money)



