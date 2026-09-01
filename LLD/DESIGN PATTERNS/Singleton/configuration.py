class Configs:
    _instance_object = None
    some_variable = 10

    def __new__(cls, db, secret):
        if cls._instance_object is None:
            # matlab object abhi khali hai
            cls._instance_object = super().__new__(cls)

            # matlab memmory me object (_instance_object) ke liye space ban gyi
            # or uske andar ek variable some_variable = 10 hoga

            cls._instance_object._initialized = False
        return cls._instance_object

    def __init__(self, db, secret) -> None:
        if self._initialized == False:
            self.db = db
            self.secret = secret
            self._initialized = True
        return


if __name__ == "__main__":
    s1 = Configs("one", "Two")
    s2 = Configs("three", "four")

    print(s1.db)
    print(s1.secret)
    print(s2.db)
    print(s2.secret)

    pass
