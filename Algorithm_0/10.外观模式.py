# 子类：子接口
class CPU:
    def run(self):
        print('CPU start run.')

    def runstop(self):
        print('CPU stop run.')

# 子类：子接口
class Disk:
    def run(self):
        print('Disk start run.')

    def runstop(self):
        print('Disk stop run.')

# 高级类：统一管理子类，用户只需要调用此类便可以管理disk与CPU;此高级类称为外观
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()

    def run(self):
        self.cpu.run()
        self.disk.run()

    def stop(self):
        self.disk.runstop()
        self.cpu.runstop()


computer = Computer()
computer.run()
computer.stop()



