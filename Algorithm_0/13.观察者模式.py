from abc import abstractmethod, ABCMeta


# 订阅者
class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def DataUpdate(self, noticeMsg):  # 接收到Notice报文后需要更新数据
        pass

# 发布者
class Publiser(metaclass=ABCMeta):
    @abstractmethod
    def ServiceBind(self, subscriber):  # 接收到Notice报文后需要更新数据
        pass

    @abstractmethod
    def SeviceRelease(self, subscriber):
        pass

    @abstractmethod
    # noitice报文发送给所有的订阅者
    def SendNotice(self, data):
        pass

# 定义Notice报文
class NoticeMessage():
    def __init__(self,data = 0):
        self.__data = data  # 私有属性

    @property
    def GetData(self):
        return self.__data

    @GetData.setter # 报文的属性不可以被外来的接口更改
    def SetData(self,data):
        self.__data = data

# 实际的订阅者：下挂ECU
class SlaverECU(Subscriber):
    def __init__(self, name = None,data = 0):
        self.name = name
        self.data = data

    def DataUpdate(self, noticeMsg):
        self.data = noticeMsg.GetData # 更新自己得到的数据

# 实际的发布者：网关
class GateWay(Publiser):
    def __init__(self):
        self.subscriber = []  # 保存自己的订阅者
        self.noticeMsg = NoticeMessage()

    # 服务绑定
    def ServiceBind(self, subscriber):
        print("Bind %s success" % subscriber.name)
        self.subscriber.append(subscriber)

    # 服务释放
    def SeviceRelease(self, subscriber):
        print("Release %s success" % subscriber.name)
        self.subscriber.remove(subscriber)

    # noitice报文发送给所有的订阅者
    def SendNotice(self, data):
        self.noticeMsg.SetData = data  # 更新notice报文数据并发送
        for obj in self.subscriber:
            obj.DataUpdate(self.noticeMsg)

ECU1 = SlaverECU("CCU")
ECU2 = SlaverECU("SCU")
GW = GateWay()
print("ECU1 data = %d" % ECU1.data)
print("ECU2 data = %d" % ECU2.data)

# 订阅者绑定
GW.ServiceBind(ECU1)
GW.ServiceBind(ECU2)

# 数据更新
GW.SendNotice(555)
print("ECU1 data = %d" % ECU1.data)
print("ECU2 data = %d" % ECU2.data)

# 订阅者释放
GW.SeviceRelease(ECU1)
GW.SeviceRelease(ECU2)
