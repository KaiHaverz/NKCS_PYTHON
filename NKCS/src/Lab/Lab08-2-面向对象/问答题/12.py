class StarkConfig(object):
    def __init__(self, num):
        self.num = num

    def changelist(self, request):
        print(self.num, request)

    def run(self):
        self.changelist(999)

class RoleConfig(StarkConfig):
    def changelist(self, request):
        print(777, self.num)

config_obj_list = [StarkConfig(1), StarkConfig(2), StarkConfig(3)]
config_obj_list[1].run()
config_obj_list[2].run()