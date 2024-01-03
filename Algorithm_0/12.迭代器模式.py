from abc import abstractmethod, ABCMeta


# 每个请求处理者都应该有处理函数
class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, days):
        pass


class GeneralManager(Handler):
    def handle_leave(self, days):
        print("总经理已接收：")
        if days <= 10:
            print("总经理准假 %d 天" % days)
        else:
            print('你还是辞职吧')


class DepartManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, days):
        print("部门经理已接收：")
        if days <= 3:
            print("部门经理准假 %d 天" % days)
        else:
            print('转至总经理处理--')
            self.next.handle_leave(days)


de = DepartManager()
de.handle_leave(8)


