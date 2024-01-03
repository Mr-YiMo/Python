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


# 工厂接口基类
class PayBasicInterFaceFactory(metaclass=ABCMeta):
    @abstractmethod
    def creat_payment(self):
        raise NotImplementedError


# 工厂类
class AliPayFactory(PayBasicInterFaceFactory):
    # 工厂函数
    def creat_payment(self):
        return AliPay()


# 工厂类
class WeChatPayFactory(PayBasicInterFaceFactory):
    # 工厂函数
    def creat_payment(self):
        return WeChatPay()


ali_pf = AliPayFactory()
p = ali_pf.creat_payment()
p.pay(100)

we_pf = WeChatPayFactory()
p = we_pf.creat_payment()
p.pay(100)
