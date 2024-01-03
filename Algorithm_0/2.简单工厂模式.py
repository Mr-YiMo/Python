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

class PayBasicInterFaceFactory(object):
    def creat(self):
        raise NotImplementedError

# 工厂类
class PayFactory:
    # 工厂函数
    def creat_payment(self,method):
        if method == 'AliPay':
            return AliPay()
        elif method == 'WeChatPay':
            return WeChatPay()
        else:
            raise TypeError("No such payment named %s" % method)


pf = PayFactory() # 实例化工厂
p = pf.creat_payment('AliPay') #制造支付方式
p.pay(100)