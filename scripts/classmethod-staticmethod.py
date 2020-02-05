
class Test:
    # class variable
    i = 4

    @classmethod
    def get_i(cls):
        return cls.i

    @staticmethod
    def output():
        print(Test.get_i())


if __name__ == '__main__':
    Test.output()
