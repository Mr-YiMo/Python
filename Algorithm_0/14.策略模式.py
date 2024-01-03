from abc import abstractmethod, ABCMeta


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass


class FastStrategy(Strategy):
    def execute(self, data):
        print("使用快速测试略处理数据： %s" % data)


class SlowStrategy(Strategy):
    def execute(self, data):
        print("使用慢速测试略处理数据： %s" % data)


# 封装策略：将所有的数据和策略集中处理
class Context():
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)


data = "aiosyudiqhirjhiuy"
fs = FastStrategy()
ls = SlowStrategy()
context = Context(fs, data)
context.do_strategy()
# 切换策略
context.set_strategy(ls)
context.do_strategy()
