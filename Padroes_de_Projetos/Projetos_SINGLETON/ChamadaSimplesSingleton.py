class Singleton(object):
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instace = super(Singleton, cls).__new__(cls)
        return cls.instace

s = Singleton()
print("Object created", s)

s1 = Singleton()
print("Object created", s1)