from abc import ABCMeta, abstractmethod


class Player:
    def __init__(self, face, arm, leg):
        self.face = face
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return '%s,%s,%s' % (self.face, self.arm, self.leg)


# 抽象基类：工厂方法接口
class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass


# 特定的产品
class SexyGileBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player("", "", "")

    def build_face(self):
        self.player.face = '瓜子脸'

    def build_arm(self):
        self.player.arm = '细胳膊'

    def build_leg(self):
        self.player.leg = '大长腿'


# 制定组装顺序
class PlayerDirect:
    def buildPlayer(self, builder):
        builder.build_face()  # 先组装脸
        builder.build_leg()  # 再组装腿
        builder.build_arm()  # 后组装胳膊
        return builder.player


builder = SexyGileBuilder()
direct = PlayerDirect()
p = direct.buildPlayer(builder)
print(p)
