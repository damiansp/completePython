class Singleton:
    _instance = None


    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


s1 = Singleton.get_instance()
s2 = Singleton.get_instance()
print(s1 is s2)
