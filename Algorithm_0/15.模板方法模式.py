from abc import abstractmethod, ABCMeta
import time

class Windows(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def repaint(self):
        pass

    @abstractmethod
    def stop(self): # 具体制定变的东西
        pass

    # 这个在抽象类的具体方法就是模板方法,也就是不变的东西
    def run(self):
        while True:
            try:
                self.repaint()
                time.sleep(1)
            except KeyboardInterrupt:
                break
        self.stop()

class MyWindows(Windows):
    def __init__(self,msg):
        self.msg =msg

    def start(self):
        print('start run')

    def repaint(self):
        print('message: %s' % self.msg)

    def stop(self):
        print('stop run')

    # 不需要再实现run
    # def run(self):
    #     while True:
    #         try:
    #             self.repaint()
    #             time.sleep(1)
    #         except KeyboardInterrupt:
    #             break
    #     self.stop()

MyWindows("12456").run()