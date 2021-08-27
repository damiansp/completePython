class Demo:
    @classmethod
    def class_meth(*args):
        return args

    @staticmethod
    def stat_meth(*args):
        return args

print(Demo.class_meth())
print(Demo.class_meth('spam'))
print(Demo.stat_meth())
print(Demo.stat_meth('spam'))
